"""
File: analysis.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    Application of a very simple model for a cup of coffee cooling off.

    This is a Python script that compares analytical and numerical 
    solutions and shows the effect of different heat transfer 
    coefficient values (the h parameter in the models). Results 
    are plotted and saved as png files in the working directory.
"""

# Import modules
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

# Import cooling model functions from cooling_mods.py
import cooling_mods as cm

# Reload it after making changes to function code
reload(cm)

# Times, up to 60 min (s)
dt = 1
maxtime = 60
times = np.arange(0, maxtime + dt, dt) * 60
times

# Call and compare analytical and numerical versions
# See cooling_mods.py module for units
Tc_an = cm.lc_cool_an(T_init = 80, T_air = 20, mass = 300, area = 0.026, h = 25, times = times)
Tc_nu = cm.lc_cool_nu(T_init = 80, T_air = 20, mass = 300, area = 0.026, h = 25, times = times)
Tc_eu = cm.lc_cool_eu(T_init = 80, T_air = 20, mass = 300, area = 0.026, h = 25, time_range = (0., maxtime * 60), dt = dt * 60)

# Plot predictions
plt.close()
plt.plot(times / 60, Tc_an, 'r-', label = 'Analytical')
plt.plot(times / 60, Tc_nu, 'b:', label = 'Numerical')
plt.plot(times / 60, Tc_eu, 'r.', label = 'Explicit Euler')
plt.legend()
plt.xlabel('Time (min)')
plt.ylabel('Predicted coffee temperature $(^\circ\mathregular{C})$')
plt.savefig('coffee_temp_mod_comp.png')

# Call model function with some different h values
Tc1 = cm.lc_cool_an(T_init = 80, T_air = 20, mass = 300, area = 0.026, h = 25, times = times)
Tc2 = cm.lc_cool_an(T_init = 80, T_air = 20, mass = 300, area = 0.026, h = 50, times = times)
Tc3 = cm.lc_cool_an(T_init = 80, T_air = 20, mass = 300, area = 0.026, h = 75, times = times)
Tc4 = cm.lc_cool_an(T_init = 80, T_air = 20, mass = 300, area = 0.026, h = 100, times = times)
Tc5 = cm.lc_cool_an(T_init = 80, T_air = 20, mass = 300, area = 0.026, h = 200, times = times)

# Plot predictions
plt.close()
plt.plot(times / 60, Tc1, label = '25')
plt.plot(times / 60, Tc2, label = '50')
plt.plot(times / 60, Tc3, label = '75')
plt.plot(times / 60, Tc4, label = '100')
plt.plot(times / 60, Tc5, label = '200')
plt.legend()
plt.xlabel('Time (min)')
plt.ylabel('Predicted coffee temperature (°C)')
plt.savefig('coffee_temp_h.png')

