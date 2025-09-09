"""
File: cooling_mods.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    Functions that implement simple lumped capacitance models for 
    predicting cooling of e.g., a cup of coffee.
"""

import numpy as np
from scipy.integrate import solve_ivp

def lc_cool_an(T_init, T_air, mass, area, h, times, cp=4.2):

    """
    Analytical implementation of a lumped capacitance cooling model.

    Parameters
    ----------
    T_init : float
        Initial temperature of the cooling object (°C).
    T_air : float
        Ambient (air) temperature (°C).
    mass : float
        Mass of the object (kg).
    area : float
        Heat transfer area (m2).
    h : float
        Heat transfer coefficient (W/m2-K).
    times : array or list
        Times at which to evaluate the solution (s).
    cp : float, optional
        Specific heat capacity (kJ/kg-K). Default is 4.2.

    Returns
    -------
    np.ndarray
        Predicted temperatures at the given times (degrees C).
    """

    # Make sure times are in an array for vectorized calculations
    times = np.array(times)

    # Calculate the constant that combines some variables and parameters
    cc = area * h / (cp * mass)

    # And the solution
    Tt = (T_init - T_air) * np.exp(-cc * times) + T_air

    # Return solution
    return Tt

def lc_cool_nu(T_init, T_air, mass, area, h, times, cp=4.2):
    """
    Numerical implementation of a lumped capacitance cooling model.
    Uses solve_ivp() with default settings (RK45).
    """

    # Define rates function
    def rates(t, T_current):
        # Calculate the constant that combines some variables and parameters
        cc = area * h / (cp * mass)
        return - cc * (T_current - T_air)

    # Make sure times are in an array for vectorized calculations
    times = np.array(times)

    # And use the finite difference method with solve_ivp() defaults
    res = solve_ivp(rates, t_span = (min(times), max(times)), y0 = [T_init], t_eval = times)

    # Let's just extract the predicted temperature
    Tt = res.y[0, :]

    # Return solution
    return Tt


def lc_cool_eu(T_init, T_air, mass, area, h, time_range, dt, cp=4.2):
    """
    Numerical implementation of a lumped capacitance cooling model.
    This version is based on the explict forward Euler's method.
    It is not a very good method, and is included here for comparison
    and to help with understanding the finite difference method.
    And it can be sufficient for some models!
    """

    # Calculate constant, which does not change over time
    cc = area * h / (cp * mass)

    # Create vector of times and concentrations
    times = np.arange(time_range[0], time_range[1] + dt, dt)
    Tt = np.zeros_like(times)
    Tt[0] = T_init

    # Implement an explicit forward finite difference method in a loop
    for i in range(1, len(Tt)):
        Tt[i] = Tt[i - 1]  - cc * (Tt[i - 1] - T_air) * dt

    # Return solution
    return Tt

