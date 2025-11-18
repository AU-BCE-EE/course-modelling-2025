"""
File: O2dc_cell_mods.py
Authors: Frederik R. Dalby and Sasha D. Hafner
Course: Modelling 2025

Description:
    A model for oxygen diffusion and consumption in a bacterial culture.
    Cell-based approach! The name dc = diffusion and consumption.
"""

import numpy as np 
from scipy.integrate import solve_ivp

def O2dcc(
    L,
    N,
    k,
    tmax,
    nt =      20,
    S_init  =  0.01,
    O2_init =  0.01,
    O2_sat   = 0.01,
    D = {
        "O2": 2.1E-9,
        "S": 1.5E-9
    }
):

    """
    Dynamic model for dissolved oxygen diffusion and BOD degradation 
    in a stagnant mixture. BOD degradation modeled as a second-order
    reaction. This is a cell-based version.

    Parameters
    ----------
    L : float
        Total water column depth (m)
    N : int
        Number of cells in model grid
    k : float
        Second-order rate constant for BOD oxidation (m3/kg-s)
    tmax : float
        Duration of simulation (s)
    nt : int
        Number of evenly spaced times to include in output
    S_init : float
        Initial uniform BOD concentration (kg/m3)
    O2_init : float
        Initial uniform O2 concentration (kg/m3)
    O2_sat : float
        Saturation O2 concentration (kg/m3)
    D : dictionary of two floats
        Diffusivity of O2 and BOD with names 'O2' and 'S' (kg/m3)

    Returns
    -------
    dictionary
        With elements 't' for time (s), 'dx' for cell center spacing, 'x' 
        for cell positions, 'O2' for O2 concentration (kg/m3), 'S'
        for BOD concentration, and 'O2in' for cumulative mass 
        transfer of O2 through the upper surface (kg/m2).
    """

    # Define rates function
    def rates(t, y):
        """
        Internal function for calculating derivatives. Uses objects present 
        in main function namespace.

        Parameters
        ----------
        t : float
            Time (s)
        y : array
            State variable array with O2 concentration (first N 
            cells), BOD concentration (next N cells), and 
            cumulative mass transfer of O2 through upper surface 
            (last element)
        """

        # Arrays to hold derivatives
        dO2dt = np.zeros(N)
        dSdt = np.zeros(N)

        # And fluxes for intermediate calculations
        # These are between all cells, so N - 1
        J_O2 = np.zeros(N + 1)
        J_S = np.zeros(N + 1)
        
        # Extract concentrations
        O2 = y[:N]
        S = y[N:-1]

        # Extend with boundary conditions for easier calculations
        O2 = np.insert(O2, 0, O2_sat)
        S = np.insert(S, 0, S[0])

        # Fluxes (kg/m2-s)
        for i in range(N):
            J_O2[i] = -D["O2"] * (O2[i + 1] - O2[i]) / dxi[i]
            J_S[i] = -D["S"] * (S[i + 1] - S[i]) / dxi[i]

        # Leave final [N + 1] fluxes zero (no-flow bottom) 

        # Respiration (kg/m3-s)
        # Can be done like this because calculation is exactly the same for every cell
        respir = k * O2 * S

        # Combine flux differences and respiration for concentration derviatives (kg/m3-s)
        for i in range(N):
            dO2dt[i] = (J_O2[i] - J_O2[i + 1]) / dx - respir[i]
            dSdt[i]  = (J_S[i]  -  J_S[i + 1]) / dx - respir[i]

       # Flux of O2 in between first two cell
        J_in_O2 = J_O2[0]
          
        # Combine derivatives for O2 and substrate together in one array
        dydt = np.concatenate((dO2dt, dSdt))

        # And stick the O2 surface flux on the end
        dydt = np.append(dydt, J_in_O2)

        # And return them all
        return dydt

    # Now to solve the model we need to sort out some inputs

    # Cell spacing, N is number of cells
    dx = L / N
    dxi = np.full(N + 1, dx)
    dxi[[0, -1]] = dx / 2

    # Initial state variable values
    O20 = np.full(N, O2_init)
    S0 = np.full(N, S_init)

    # Combine state variables, including cumulative O2 diffusion at the end
    y0 = np.concatenate((O20, S0))
    y0 = np.append(y0, 0.)

    # Have solve_ivp() do the work of integration
    sol = solve_ivp(
        rates, 
        t_span = [0., tmax], 
        y0 = y0, 
        t_eval = np.linspace(0., tmax, nt)
    )

    # Cell center positions
    xa = np.linspace(0, L, N) + dx / 2

    # Extract and organize the results in a dictionary
    out = {
        "t": sol.t,
        "dx": dx,
        "x": xa,
        "O2": sol.y[:N, ],
        "S":  sol.y[N:2*N, ],
        "O2in":  sol.y[-1, ]
    }

    # Return them
    return out
