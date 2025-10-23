
"""
File name: amm_mods.py
Author: Sasha D. Hafner and Frederik Dalby
Course: Modelling 2025

Description:
    This module defines functions for modeling ammonia volatilization
    from a slurry storage tank. This version has some deliberate 
    **errors**!

Usage:
    See amm_demo.py.

"""

# Load packages 
import numpy as np
from scipy.integrate import solve_ivp

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def dynmod(rt,
           depth,
           c_TAN_in,
           c_urea_in,
           c_TAN_0,
           c_urea_0,
           c_bg,
           pH,
           ku,
           kl,
           times, 
           hen = 2000.,
           pka = 9.24):
    """ 
    Dynamic model for ammonia volatilization from a manure storage 
    tank with constant and equal manure flow in and out and a constant
    volume of manure. Includes urea hydrolysis.

    Parameters
    ----------
    rt : float
        Retention time of manure in the tank (s)
    depth : float
        Depth of manure in the tank (m).
    c_TAN_in : float
        Concentration of TAN in fresh manure (kg/m3 as N).
    c_urea_in : float
        Concentration of urea in fresh manure (kg/m3 as N).
    c_TAN_0 : float
        Initial concentration of TAN in tank (kg/m3 as N).
    c_urea_0 : float
        Initial concentraiton of urea in tank (kg/m3 as N).
    c_bg : float
        Converted concentration of NH3 (g) in ambient (background) 
        air (kg/m3 as N in aqueous phase).
    pH : float
        Manure pH (pH units).
    ku : float
        First-order reaction rate constant for urea hydrolysis (1/s).
    kl : float
        Overall liquid-phase mass transfer coefficient (m/s).
    t_range : tuple, list, or array (length 2)
        Initial and final time requested in output (s).
    t_step : float
        Time step requested for output (s).
    hen : float
        Henry's law constant (dimensionless, aq:g).
    pka : float
        Negative log_10 of the equilibrium constant 
        (acid dissociation constant) for NH4+ -> NH3 + H +
        (dimensionless).

    Output
    ------
    t : array
        Time (s)
    tan : array
        TAN concentration in the tank (kg/m3)
    urea : array
        Urea concentration in the tank (kg/m3)
    """
  
    # Sort out some constants
    frac_NH3 = 1/(1 + 10**(pka - pH))

    # Define rates function
    def rates(t, conc):
        """
        Calculates derviatives of TAN and urea concentration in tank
        as kg/m3-s as nitrogen.

        Parameters
        ----------
        t : float
            time (s) (not used in function)
        conc : list of two floats
            TAN and urea concentration in tank (kg/m3)
        """

        c_TAN = conc[0]
        c_urea = conc[1]

        TAN_in = c_TAN_in / rt
        TAN_out = c_TAN / rt

        urea_in = c_urea_in / rt
        urea_out = c_urea / rt

        urea_hyd = ku * c_urea

        volat = kl / depth * (frac_NH3 * c_TAN - c_bg * hen)

        dc_TAN_dt = TAN_in - TAN_out + urea_hyd - volat
        dc_urea_dt = urea_in - urea_out 

        return np.array([dc_TAN_dt, dc_urea_dt])

    # Now solve with solve_ivp()
    res = solve_ivp(rates, t_span = [min(times), max(times)], 
                    y0 = [c_TAN_0, c_urea_0], t_eval = times)

    # Return results in dictionary
    out = {"t": res.t, 'tan': res.y[0, :], 'urea': res.y[1, :]}

    return(out)

def ddynmod(f_in,
            f_out,
            a_top,
            c_TAN_0,
            c_urea_0,
            c_bg,
            pH,
            ku,
            kl,
            t_range, 
            t_step,
            m_TAN_0 = 0.,
            m_urea_0 = 0.,
            m_man_0 = 1.E-6,
            hen = 2000.,
            pka = 9.24):
    """ 
    Dynamic model for ammonia volatilization from a manure storage 
    tank with constant but possibly unequal manure flow in and out 
    and a variable volume of manure. Includes urea hydrolysis.

    Parameters
    ----------
    f_in : float
        Rate of manure pumping into tank (m3/s)
    f_out : float
        Rate of manure pumping out of tank (m3/s)
    a_top : float
        Area of tank (top and at any depth) (m2).
    c_TAN_0 : float
        Concentration of TAN in fresh manure (kg/m3 as N).
    c_urea_0 : float
        Concentration of urea in fresh manure (kg/m3 as N).
    c_bg : float
        Converted concentration of NH3 (g) in ambient (background) 
        air (kg/m3 as N in aqueous phase).
    pH : float
        Manure pH (pH units).
    ku : float
        First-order reaction rate constant for urea hydrolysis (1/s).
    kl : float
        Overall liquid-phase mass transfer coefficient (m/s).
    t_range : tuple, list, or array (length 2)
        Initial and final time requested in output (s).
    t_step : float
        Time step requested for output (s).
    hen : float
        Henry's law constant (dimensionless, aq:g).
    pka : float
        Negative log_10 of the equilibrium constant 
        (acid dissociation constant) for NH4+ -> NH3 + H +
        (dimensionless).
 
    """
  
    # Sort out some constants
    frac_NH3 = 1/(1 + 10**(pka - pH))

    # Density in kg/m3
    dens = 1000

    # Define rates function
    # Now this is for mass not concentration
    def rates(t, mass):

        m_TAN = mass[0]
        m_urea = mass[1]
        m_man = mass[2]

        vol_man = m_man / dens

        TAN_in = c_TAN_0 * f_in
        TAN_out = m_TAN / vol_man * f_out

        urea_in = c_urea_0 * f_in
        urea_out = m_urea / vol_man * f_out

        urea_hyd = ku * m_urea

        volat = kl * a_top * (frac_NH3 * m_TAN / vol_man - c_bg * hen)

        dm_TAN_dt = TAN_in - TAN_out + urea_hyd - volat
        dm_urea_dt = urea_in - urea_out - urea_hyd
        dm_man_dt = (f_in  - f_out) * dens

        return np.array([dm_TAN_dt, dm_urea_dt, dm_man_dt])

    # Now solve with solve_ivp()
    res = solve_ivp(rates, t_span = t_range, y0 = [m_TAN_0, m_urea_0, m_man_0], 
                    t_eval = np.arange(t_range[0], t_range[1] + t_step, t_step))

    # That gives us masses of the three state variables
    # Let's calculate concentrations too

    # Return results in dictionary
    out = {"t": res.t, 'tan': res.y[0, :], 'urea': res.y[1, :]}

    return(out)

