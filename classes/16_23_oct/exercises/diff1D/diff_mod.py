# Load packages 
import numpy as np
from scipy.integrate import solve_ivp

def diff1D(L,       
           n,       
           D,       
           bc,      
           ci,      
           t_eval   
):  

    """
    A 1D diffusion model for rectangular geometry with flow through both boundaries.

    Parameters
    ----------
    L : float
        Total column, layer, material, etc. length or thickness (m)
    n : integer
        Number of spatial layers/cells/nodes                                                                     '
    D : float
        Diffusivity (m2/s)
    bc : list or tuple
        Boundary conditions, fixed concentrations (g/m3), bc[0] = left or bottom, bc[1] = right or top
    ci : float
        Initial concentration (single value -> uniform or flat profile)
    t_eval : list, tuple, or array
        Times for model evaluation (s)

    Returns
    -------
    dictionary
        Concentration profile (g/m3) and cumulative transfer at boundaries (g/m2) ([0] = left (or bottom), [1] = right (or top))
    """

    # Define rates function 
    def rates(t, c):
    
        # Extract the cell concentrations (remove the two values of cumulative mass transfer)
        c = c[:-2] 
    
        # Extend concentration array with the boundary condition values to make calculations easier
        ca = np.insert(c, 0, bc[0])
        ca = np.append(ca, bc[1])
    
        ## Get second differences (our approximation of second derivatives) with central difference method
        #der2 = (ca[2:] - 2 * ca[1:-1] + ca[:-2]) / dxi[1:-1]**2
        ## Then rate of concentration change in kg/m3-s
        #dcdt = D * der2

        # Or calculate in steps 
        # Flux at all interfaces between cells
        j = -D * (ca[1:] - ca[:-1]) / dxi
        # Derivative
        dcdt = (j[:-1] - j[1:]) / dx
    
        # Extract flux at first and last cell
        # Positive is right for both
        # kg/m2-s
        jb = j[[0, -1]]
    
        # And combine it with the derivative vector at the end to track cumlative transfer in and out
        der = np.append(dcdt, jb)
        
        # Return derivatives, all kg/m2-s
        return(der)

    # Extract some inputs
    t_max = max(t_eval)
    t_span = (0, t_max)

    # Initial state variable vector 
    si = np.repeat(ci, n + 2)
    # Last positions are mass loss, always with starting value of 0
    si[-2:] = 0

    # Cell width (m)
    dx = L / n 
    
    # This is a cell-based approach, so our boundary dx values are half as large as the others
    dxi = np.full(n + 1, dx)
    dxi[[0, -1]] = dx / 2

    # Solve with ODE solver
    res = solve_ivp(rates, t_span, si, t_eval = t_eval)

    # Add x positions based on cell centers 
    x = np.linspace(0, L, n) + dx / 2

    # Organize results in a dictionary
    out = {
        "t": res.t, 
        "dx": L/n, 
        "x": x, 
        "c": res.y[:-2], 
        "ml": res.y[-2], 
        "mr": res.y[-1]
    }

    return(out)
 
