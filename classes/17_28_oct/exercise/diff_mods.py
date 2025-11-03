"""
File name: diff_mods.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    This module defines numerical models for 1D diffusion of a solute
    through a column or semi-infinite slab.

Usage:
    See the diff1D_demo.py file for a demo.
"""

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
    A 1D diffusion model for rectangular geometry with flow through 
    both boundaries. This version follow's Frederik's approaches: 
    node-based, no separate flux calc. but direct use of 2nd der.
    in central difference method, and extension of concentration
    array with boundary conditions in main function not rates().

    Parameters
    ----------
    L : float
        Total column, layer, material, etc. length or thickness (m)
    n : integer
        Number of spatial nodes
    D : float
        Diffusivity (m2/s)
    bc : list or tuple
        Boundary conditions, fixed concentrations (kg/m3), bc[0] = left or bottom, bc[1] = right or top
    ci : float
        Initial concentration (single value -> uniform or flat profile)
    t_eval : list, tuple, or array
        Times for model evaluation (s)

    Returns
    -------
    dictionary
        With time (t, s), cell width (dx, m), cell center position 
        (x, m), concentration profile (c, kg/m3), and cumulative 
        mass transfer at left and right boundaries (ml, mr, kg/m2).
    """

    # Define rates function 
    def rates(t, ca):
    
        # Empty array for derivatives
        dcdt = np.zeros(len(ca))

        # Use second differences (our approximation of second derivatives) 
        # from central difference method to calculate derviatives
        for i in range(1, n):
            dcdt[i] = D * (ca[i + 1] - 2 * ca[i] + ca[i - 1]) / dx**2

        # For boundaries, derivatives are zero for Dirichlet boundary condition
        dcdt[[0, n]] = 0.

        # Add derviatives for cumulative mass transfer, i.e., fluxes at the boundaries
        dcdt[[n + 1, n + 2]] = -D * (ca[[1, n]] - ca[[0, n - 1]]) / dx 

        # Return derivatives, all kg/m2-s
        return(dcdt)

    # Extract some inputs
    t_max = max(t_eval)
    t_span = (0, t_max)

    # Initial state variable vector 
    # This includes: node concentrations (start and end with boundaries) and cumulative mass transfer
    si = np.repeat(ci, n + 3)
    # First and last nodes are boundary concentrations
    # Only because we have Dirichlet boundary conditions (fixed concentrations)
    si[[0, n]] = bc

    # Cell width (m)
    dx = L / n
    
    # Array of cell widths associated with each node
    # Here the boundary nodes have dx/2
    dxa = np.repeat(dx, n + 1)
    dxa[[0, n]] = dx / 2.
    
    # Solve with ODE solver
    res = solve_ivp(rates, t_span, si, t_eval = t_eval)

    # Add x positions for all nodes
    x = np.linspace(0, L, n + 1)

    # Organize results in a dictionary
    out = {
        "t": res.t, 
        "dx": dxa, 
        "x": x, 
        "c": res.y[:-2, :], 
        "ml": res.y[-2, :], 
        "mr": res.y[-1, :]
    }

    return(out)
 

def diff1Db(L,       
            n,       
            D,       
            bc,      
            ci,      
            t_eval   
):  

    """
    A 1D diffusion model for rectangular geometry with flow through 
    both boundaries. This version follow's Frederik's approaches: 
    node-based, no separate flux calc. but direct use of 2nd der.
    in central difference method, and extension of concentration
    array with boundary conditions in main function not rates().

    Parameters
    ----------
    L : float
        Total column, layer, material, etc. length or thickness (m)
    n : integer
        Number of spatial layers/cells (nodes = n + 1)
    D : float
        Diffusivity (m2/s)
    bc : list or tuple
        Boundary conditions, fixed concentrations (kg/m3), bc[0] = left or bottom, bc[1] = right or top
    ci : float
        Initial concentration (single value -> uniform or flat profile)
    t_eval : list, tuple, or array
        Times for model evaluation (s)

    Returns
    -------
    dictionary
        With time (t, s), cell width (dx, m), cell center position 
        (x, m), and concentration profile (c, kg/m3).
    """

    # Define rates function 
    def rates(t, ca):
    
        # Empty array for derivatives
        dcdt = np.zeros(len(ca))

        # Use second differences (our approximation of second derivatives) 
        # from central difference method to calculate derviatives
        for i in range(1, n):
            dcdt[i] = D * (ca[i + 1] - 2 * ca[i] + ca[i - 1]) / dx**2

        # For boundaries, derivatives are zero for Dirichlet boundary condition
        dcdt[[0, n]] = 0.

        # Return derivatives, all kg/m2-s
        return(dcdt)

    # Extract some inputs
    t_max = max(t_eval)
    t_span = (0, t_max)

    # Initial state variable vector 
    # This includes: node concentrations (start and end with boundaries) and cumulative mass transfer
    si = np.repeat(ci, n + 1)
    # First and last nodes are boundary concentrations
    # Only because we have Dirichlet boundary conditions (fixed concentrations)
    si[[0, n]] = bc

    # Cell width (m)
    dx = L / n 
    
    # Array of cell widths associated with each node
    # Here the boundary nodes have dx/2
    dxa = np.repeat(dx, n + 1)
    dxa[[0, n]] = dx / 2.
    
    # Solve with ODE solver
    res = solve_ivp(rates, t_span, si, t_eval = t_eval)

    # Add x positions for all nodes
    x = np.linspace(0, L, n + 1)

    # Organize results in a dictionary
    out = {
        "t": res.t, 
        "dx": dxa, 
        "x": x, 
        "c": res.y
    }

    return(out)
 

def diff1Dc(L,       
            n,       
            D,       
            bc,      
            ci,      
            t_eval   
):  

    """
    A 1D diffusion model for rectangular geometry with flow through both boundaries.
    This is actually the original version, and was previously called diff1D().
    It uses my (Sasha's) preferred cell-based approach and array-based slicing
    operations for derivatives instead of a loop.

    Parameters
    ----------
    L : float
        Total column, layer, material, etc. length or thickness (m)
    n : integer
        Number of spatial layers/cells/nodes                                                                     '
    D : float
        Diffusivity (m2/s)
    bc : list or tuple
        Boundary conditions, fixed concentrations (kg/m3), bc[0] = left or bottom, bc[1] = right or top
    ci : float
        Initial concentration (single value -> uniform or flat profile)
    t_eval : list, tuple, or array
        Times for model evaluation (s)

    Returns
    -------
    dictionary
        With time (t, s), cell width (dx, m), cell center position 
        (x, m), concentration profile (c, kg/m3), and cumulative 
        mass transfer at left and right boundaries (ml, mr, kg/m2).
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
    
        # Extract flux at first and last cell (i.e., at the boundaries)
        # Positive is right for both
        # kg/m2-s
        jbound = j[[0, -1]]
    
        # And combine it with the derivative vector at the end to track cumlative transfer in and out
        der = np.append(dcdt, jbound)
        
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
        "c": res.y[:-2, :], 
        "ml": res.y[-2, :], 
        "mr": res.y[-1, :]
    }

    return(out)
 
def diff1Dd(L,       
            n,       
            D,       
            bc,      
            ci,      
            t_eval   
):  

    """
    A 1D diffusion model for rectangular geometry with flow through both boundaries.
    This version differs from diff1Dc() in that both cumulative mass transfer 
    `ml` and `mr` are both positive into the system.

    Parameters
    ----------
    L : float
        Total column, layer, material, etc. length or thickness (m)
    n : integer
        Number of spatial layers/cells/nodes                                                                     '
    D : float
        Diffusivity (m2/s)
    bc : list or tuple
        Boundary conditions, fixed concentrations (kg/m3), bc[0] = left or bottom, bc[1] = right or top
    ci : float
        Initial concentration (single value -> uniform or flat profile)
    t_eval : list, tuple, or array
        Times for model evaluation (s)

    Returns
    -------
    dictionary
        With time (t, s), cell width (dx, m), cell center position 
        (x, m), concentration profile (c, kg/m3), and cumulative 
        mass transfer at left and right boundaries (ml, mr, kg/m2).
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
    
        # Extract flux at first and last cell (i.e., at the boundaries)
        # Positive is right for both
        # kg/m2-s
        jbound = [j[0], -j[ -1]]
    
        # And combine it with the derivative vector at the end to track cumlative transfer in and out
        der = np.append(dcdt, jbound)
        
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
        "c": res.y[:-2, :], 
        "ml": res.y[-2, :], 
        "mr": res.y[-1, :]
    }

    return(out)
 
def diff1De(L,       
            n,       
            D,       
            bc,      
            ci,      
            t_eval   
):  

    """
    A 1D diffusion model for rectangular geometry with flow through both boundaries.
    This version is like diff1Dc() but uses a loop in rates().

    Parameters
    ----------
    L : float
        Total column, layer, material, etc. length or thickness (m)
    n : integer
        Number of spatial layers/cells/nodes                                                                     '
    D : float
        Diffusivity (m2/s)
    bc : list or tuple
        Boundary conditions, fixed concentrations (kg/m3), bc[0] = left or bottom, bc[1] = right or top
    ci : float
        Initial concentration (single value -> uniform or flat profile)
    t_eval : list, tuple, or array
        Times for model evaluation (s)

    Returns
    -------
    dictionary
        With time (t, s), cell width (dx, m), cell center position 
        (x, m), concentration profile (c, kg/m3), and cumulative 
        mass transfer at left and right boundaries (ml, mr, kg/m2).
    """

    # Define rates function 
    def rates(t, c):
    
        # Extract the cell concentrations (remove the two values of cumulative mass transfer)
        c = c[:-2] 
    
        # Extend concentration array with the boundary condition values to make calculations easier
        ca = np.insert(c, 0, bc[0])
        ca = np.append(ca, bc[1])
    
        # Flux at all interfaces between cells
        # Notice that `0.` is used! Use `0` and get an integer array and then 0 for all fluxes!
        j = np.full(n + 1, 0.)
        for i in range(n + 1):
            j[i] = -D * (ca[i + 1] - ca[i]) / dxi[i]

        # Derivative
        dcdt = np.full(n, 0.)
        for i in range(n):
            dcdt[i] = (j[i] - j[i + 1])/ dx
    
        # Extract flux at first and last cell (i.e., at the boundaries)
        # Positive is right for both
        # kg/m2-s
        jbound = j[[0, -1]]
    
        # And combine it with the derivative vector at the end to track cumlative transfer in and out
        der = np.append(dcdt, jbound)
        
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
        "c": res.y[:-2, :], 
        "ml": res.y[-2, :], 
        "mr": res.y[-1, :]
    }

    return(out)


