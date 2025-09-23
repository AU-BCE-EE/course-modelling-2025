
"""
File name: pool_funcs.py
Author: Sasha D. Hafner and Frederik Dalby
Course: Modelling 2025

Description:
    This module defines functions for modeling heat loss from a 
    swimming pool.

Usage:
    See the file predictions.qmd for examples.
"""

# Load packages 
import numpy as np
from scipy.integrate import solve_ivp

# Define model function
# pdm for dptm
def dynmod(a_top,    
           a_wall,       
           depth,
           q_sol,
           u_top,
           u_wall,
           temp_air,
           temp_sub,
           flow_renew,
           temp_renew,
           temp_init,
           t_range, 
           t_step,
           cp = 4180,
           dens = 1000
           ):  
    
    # Define rates function
    def rates(t, temp_pool):

        # Net energy, expressed as positive for increase 
        # One nice things about numerical solutions is you are not required to simplify the governing equation.
        # In fact it can be helpful to understand the different pathways to keep them separate


        # Calculate heat flow (W) through individual pathways
        # All are positive for heat flow in (this is arbitrary)
        Q_solar = a_top * q_sol                                     # Solar energy
        Q_top = a_top * u_top * (temp_air - temp_pool)              # Convection from top
        Q_sub = a_wall * u_wall * (temp_sub - temp_pool)            # Conduction to/from substrate (soil or whatever is there)
        Q_renew = cp * dens * flow_renew * (temp_renew - temp_pool) # Net energy coming in from renewal water
        
        # And sum them
        Q_net = Q_solar + Q_top + Q_sub + Q_renew

        # Express as temperature change
        dtemp_dt = Q_net / (cp * dens * vol)

        return dtemp_dt

    # Total water volume (m3)
    vol = a_top * depth

    # Now solve with solve_ivp()
    res = solve_ivp(rates, t_span = t_range, y0 = [temp_init], 
                    t_eval = np.arange(t_range[0], t_range[1] + t_step, t_step))

    # Return results
    return(res)
 
# Steady-state model
def ssmod(a_top,    
          a_wall,       
          depth,
          q_sol,
          u_top,
          u_wall,
          temp_air,
          temp_sub,
          flow_renew,
          temp_renew,
          cp = 4180,
          dens = 1000
          ):  
 
    vol = a_top * depth

    K = (a_top * u_top + 
         a_wall * u_wall + 
         cp * dens * flow_renew) / (cp * dens * vol)

    C = (q_sol * a_top + 
         a_top * u_top * temp_air +
         a_wall * u_wall * temp_sub +
         cp * dens * flow_renew) / (cp * dens * vol)

    temp_pool = C / K

    return temp_pool
