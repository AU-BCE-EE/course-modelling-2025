"""
File: melt_demo.py

Author: Sasha D. Hafner 

Description:
    Demo of a new ice melting model with time-variable inputs.
"""

# Python packages
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
import pandas as pd

# Our module
import ice_mods as im

reload(im)

# Make up some air temperature data
air_temp = pd.DataFrame(
    {
        "time": 3600 * np.linspace(0, 3, 5),
        "temp": np.linspace(5, 30, 5),
    }
)

air_temp

air_temp.loc[2, "temp"] = 28

air_temp

# These might normally be measured!

pred00 = im.melt(
    mass_0 = 0.050, 
    air_temp = 20, 
    h = 120, 
    times = 3600 * np.linspace(0, 3, 70),
)

# Now try model
pred01 = im.meltv(
    mass_0 = 0.050, 
    air_temp_dat = air_temp, 
    h = 120, 
    times = 3600 * np.linspace(0, 3, 70),
)

pred02 = im.meltv(
    mass_0 = 0.050, 
    air_temp_dat = air_temp, 
    h = 120, 
    times = 3600 * np.linspace(0, 3, 70),
    interp_kind = "cubic",
)

pred01
pred01["air_temp"]
1000 * pred01["ice_mass"]

# Plot predictions
plt.close()
plt.plot(pred01["time"] / 3600, 1000 * pred01["ice_mass"], label="Linear temp.")
plt.plot(pred02["time"] / 3600, 1000 * pred02["ice_mass"], label="Cubic temp.")
plt.xlabel("Time (h)")
plt.ylabel("Ice mass (g)")
plt.legend()
plt.savefig("plots/mod_ice_mass.png")

plt.close()
plt.plot(pred01["time"] / 3600, pred01["air_temp"], label="Linear temp.")
plt.plot(pred02["time"] / 3600, pred02["air_temp"], label="Cubic temp.")
plt.xlabel("Time (h)")
plt.ylabel("Air temperature (deg. C)")
plt.legend()
plt.savefig("plots/mod_air_temp.png")

# Some warnings:
# 1. Linear interpolation can challenge `solve_ivp()` because of kinks, but is simpler
# 2. With cubic interpolation, watch out for implausible values or 
#    values that model cannot handle--good practice to export as in example
