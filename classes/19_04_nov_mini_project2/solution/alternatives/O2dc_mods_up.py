import numpy as np 
from scipy.integrate import solve_ivp

def O2dc_b(L, 
              dx, 
              k,
              tmax,
              nt,
              O2_init, 
              S_init, 
              O2_sat, 
              D):
    
  
    def rates(t, y, dx, x_grid, O2_sat, k, D):
        
        N = len(x_grid)
        dO2dt = np.zeros(N)
        dSdt = np.zeros(N)
        
        O2 = y[:N]
        S = y[N:2*N]
        
        # For O2, BC is Dirichlet at top
        dO2dt[-1] = D["O2"] * ((O2[-2] - 2 * O2[-1] + O2_sat) / dx**2)
        # For S, BC is Neumann at top with zero flux. Substitute ghost point. 
        dSdt[-1] = D["S"] * ((S[-2] - 2 * S[-1] + S[-2]) / dx**2)

        # BC is Neumann at bottom with zero flux for both. Substitute the O2[N+1] ghost point.  
        dO2dt[0] = D["O2"] * ((O2[1] - 2 * O2[0] + O2[1]) / dx**2)
        dSdt[-1]  = D["S"]  * (( S[1] - 2 * S[0]  +  S[1]) / dx**2)
        
        # Inner nodes, use loop with central difference method
        for i in range(1, N - 1):
            dO2dt[i] = D["O2"] * ((O2[i-1] - 2 * O2[i] + O2[i+1]) / dx**2)
            dSdt[i]  = D["S"]  * ((S[i-1]  - 2 *  S[i]  + S[i+1]) / dx**2)

        # Add oxidation of substrate
        # Can be done like this because calculation is exactly the same for every node
        # Top node has constant O2 concentration though, so derivative must be zero
        # But S oxidation is using some -> see surface flux correction below
        respir = k * O2 * S
        dO2dt = dO2dt - respir
        dSdt = dSdt - respir
        # Could use -= above
        
        # Flux of O2 through first node O2[0]
        J_in_O2 = -D["O2"] * (O2[-2] - O2_sat) / (2*dx)
        J_out_O2 = -D["O2"] * (O2[1] - O2[1]) / (2*dx)
        
        fluxes = np.array([J_in_O2, J_out_O2])
        # Combine derivatives for O2 and substrate together in one array
        dydt = np.concatenate((dO2dt, dSdt))

        # And stick the O2 surface flux on the end
        dydt = np.append(dydt, fluxes)

        # And return them all
        return dydt

# Now to solve the model we need to sort out some inputs
    x_grid = np.arange(0, L + dx, dx)

# Initial state variable values
    O20 = np.zeros(len(x_grid))
    O20[:] = O2_init
    S0 = np.zeros(len(x_grid))
    S0[:] = S_init
    
# Combine state variables
    y0 = np.concatenate((O20, S0))
# add state var for the O2 flux
    y0 = np.append(y0, [0., 0.])
# Have solve_ivp()
    sol = solve_ivp(
        rates, 
        t_span = [0., tmax], 
        y0 = y0, 
        method = "LSODA",
        t_eval = np.linspace(0, tmax, nt), 
        args = (dx, x_grid, O2_sat, k, D))

    O2 = sol.y[:len(x_grid),:]
    S = sol.y[len(x_grid):(2*len(x_grid)),:]
    O2_flux_in = sol.y[-2,:]
    O2_flux_out = sol.y[-1,:]
    t = sol.t
    x = x_grid

    return {
        "O2": O2,
        "S": S,
        "O2_flux_in" : O2_flux_in,
        "O2_flux_out": O2_flux_out,
        "t" : sol.t,
        "x" : x_grid,
        "dx": dx
    }