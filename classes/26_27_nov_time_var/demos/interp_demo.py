"""
File name: melt_mods.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    This script is a demo of interpolation.

Usage:
    See the melt_demo.py file for examples.
"""

# Load packages 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Create some air temperature data
temp_air = pd.DataFrame(
    {
        "time": 3600 * np.linspace(0, 3, 5),
        "temp": np.linspace(5, 30, 5),
    }
)

temp_air.loc[2, "temp"] = 28

# Plot "measurements"
plt.close()
plt.plot(temp_air.time, temp_air.temp, "ro")
plt.xlabel("Time (s)")
plt.ylabel("Air temperature (deg. C)")
plt.savefig("plots/meas_air_temp.png")

# Create spline function with the make_splrep() function (two functions!)
air_temp_func_lin = interp1d(temp_air.time, temp_air.temp, kind="linear")
air_temp_func_cub = interp1d(temp_air.time, temp_air.temp, kind="cubic")

interp_dat = pd.DataFrame({"time": 3600 * np.linspace(0, 3, 100)})
interp_dat["temp_lin"] = air_temp_func_lin(interp_dat.time)
interp_dat["temp_cub"] = air_temp_func_cub(interp_dat.time)
interp_dat

# Add interpolated values to plot
plt.close()
plt.plot(interp_dat.time, interp_dat.temp_lin, "b-", label = "Linear")
plt.plot(interp_dat.time, interp_dat.temp_cub, "k-", label = "Cubic")
plt.plot(temp_air.time, temp_air.temp, "ro")
plt.xlabel("Time (s)")
plt.legend()
plt.ylabel("Air temperature (deg. C)")
plt.savefig("plots/interp_air_temp.png")




