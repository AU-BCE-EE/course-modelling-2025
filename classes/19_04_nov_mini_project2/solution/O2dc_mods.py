"""
File: O2dc_mods.py
Authors: Frederik R. Dalby and Sasha D. Hafner
Course: Modelling 2025

Description:
    A model for oxygen diffusion and consumption in a bacterial culture.
    Node-based approach. The name dc = diffusion and consumption. And
    O2 is oxygen of course.
"""

import numpy as np 
from scipy.integrate import solve_ivp

def O2dc(
    L, 
    dx, 
    k,
    tmax,
    nt,
    O2_init, 
    OM_init, 
    O2_sat, 
    D
):

    """
    Dynamic model for dissolved oxygen diffusion and BOD degradation 
    in a stagnant mixture. BOD degradation modeled as a second-order
    reaction. This is a node-based version.

    Parameters
    ----------
    L : float
        Total water column depth (m)
    dx: float
        Distance between nodes (m)
    k : float
        Second-order rate constant for BOD oxidation (m3/kg-s)
    tmax : float
        Duration of simulation (s)
    nt : int
        Number of evenly spaced times to include in output
    O2_init : float
        Initial uniform O2 concentration (kg/m3)
    OM_init : float
        Initial uniform BOD concentration (kg/m3)
    O2_sat : float
        Saturation O2 concentration (kg/m3)
    D : dictionary of two floats
        Diffusivity of O2 and BOD with names 'O2' and 'OM' (kg/m3)

    Returns
    -------
    dictionary
        With elements 't' for time (s), 'dx' for cell center spacing, 'x' 
        for cell positions, 'O2' for O2 concentration (kg/m3), 'OM'
        for BOD concentration, and 'O2in' for cumulative mass 
        transfer of O2 through the upper surface (kg/m2).
    """
  
    def rates(
        t, 
        y, 
        dx, 
        x_grid, 
        O2_sat, 
        k, 
        D
    ):
        
        """
        Internal function for calculating state variable derivatives.

        Parameters
        ----------
        t : float
            Time for evaluation of derivatives (s)
        y : array
            State variable values, O2 and OM concentrations for all nodes (kg/m3) 
        dx : float
            Node spacing (m)
        x_grid : array
            Grid of node positions (m) (used only for length)
        O2_sat : float
            O2_sat from main function
        k : float
            k from main function
        D : float
            D from main function


        Returns
        -------
        array
            With derivatives for each state variable
        """

        N = len(x_grid)
        dO2dt = np.zeros(N)
        dOMdt = np.zeros(N)
        
        # Extract state variable arrays
        O2 = y[:N]
        OM = y[N:2*N]
        
        # For O2, BC is Dirichlet at top
        dO2dt[0] = D["O2"] * ((O2[1] - 2 * O2[0] + O2_sat) / dx**2)
        # For OM, BC is Neumann at top with zero flux. Substitute ghost point. 
        dOMdt[0] = D["OM"] * ((OM[1] - 2 * OM[0] + OM[1]) / dx**2)

        # BC is Neumann at bottom with zero flux for both. Substitute the O2[N+1] ghost point.  
        dO2dt[-1] = D["O2"] * ((O2[-2] - 2 * O2[-1] + O2[-2]) / dx**2)
        dOMdt[-1]  = D["OM"]  * (( OM[-2] - 2 * OM[-1]  +  OM[-2]) / dx**2)
        
        # Inner nodes, use loop with central difference method
        for i in range(1, N - 1):
            dO2dt[i] = D["O2"] * ((O2[i-1] - 2 * O2[i] + O2[i+1]) / dx**2)
            dOMdt[i]  = D["OM"]  * ((OM[i-1]  - 2 *  OM[i]  + OM[i+1]) / dx**2)

        # Add oxidation of substrate
        # Can be done like this because calculation is exactly the same for every node
        respir = k * O2 * OM
        dO2dt = dO2dt - respir
        dOMdt = dOMdt - respir
        # Could use -= above
        
        # Flux of O2 through first node O2[0]
        J_in_O2 = -D["O2"] * (O2[1] - O2_sat) / (2*dx)
        
        # Combine derivatives for O2 and substrate together in one array
        dydt = np.concatenate((dO2dt, dOMdt))

        # And stick the O2 surface flux on the end
        dydt = np.append(dydt, J_in_O2)

        # And return them all
        return dydt

    # Now to solve the model we need to sort out some inputs
    x_grid = np.arange(0, L + dx, dx)

    # Initial state variable values
    O20 = np.zeros(len(x_grid))
    O20[:] = O2_init
    OM0 = np.zeros(len(x_grid))
    OM0[:] = OM_init
    
    # Combine state variables
    y0 = np.concatenate((O20, OM0))
    # Add state var for the O2 flux
    y0 = np.append(y0, 0.)

    # Have solve_ivp() solve the problem
    sol = solve_ivp(
        rates, 
        t_span = [0., tmax], 
        y0 = y0, 
        method = "LSODA",
        t_eval = np.linspace(0, tmax, nt), 
        args = (dx, x_grid, O2_sat, k, D))

    # Unpack output from solve_ivp()
    O2 = sol.y[:len(x_grid),:]
    OM = sol.y[len(x_grid):(2*len(x_grid)),:]
    O2_in = sol.y[-1,:]
    t = sol.t

    # And finally return all results in a dictionary
    return {
        "O2": O2,
        "OM": OM,
        "O2_in" : O2_in,
        "t" : sol.t,
        "x" : x_grid,
        "dx": dx
    }
