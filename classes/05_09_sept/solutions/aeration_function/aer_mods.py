"""
File: aeration_mods.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    Functions that implement numerical and analytical versions 
    of a simple model for water aeration.
"""

import numpy as np
from scipy.integrate import solve_ivp

def aer_num(kla, csat, c0, times):
    """ Numerical model with solve_ivp (RK45) """

    # Define derivatives function
    def rates(t, cc):
        return kla * (csat - cc)

    # Solve with solve_ivp()
    res = solve_ivp(rates, t_span = (min(times), max(times)), y0 = [c0], t_eval = times)

    # Let's just extract the concentrations
    conc = res.y[0, :]

    return conc

def aer_an(kla, csat, c0, times):
    """ Analytical model """

    # Make sure times is an array for vectorized calculations
    times = np.array(times)

    # Get solution
    expart = np.exp(-kla * times)
    conc = csat * (1 - expart) + c0 * expart

    # Return it
    return conc


# Numerical version with consumption
# Includes volumetric consumption rate (g/m3-h)
def aer_cons_num(kla, csat, c0, cons, times):

    # Define derivatives function
    def rates(t, cc):
        return kla * (csat - cc) - cons

    # Initial results array
    conc = np.zeros_like(times, dtype = 'float')
    conc[0] = c0

    # Solve with solve_ivp()
    res = solve_ivp(rates, t_span = (min(times), max(times)), y0 = [0], t_eval = times)

    # Let's just extract the concentrations
    conc = res.y[0, :]

    return conc




