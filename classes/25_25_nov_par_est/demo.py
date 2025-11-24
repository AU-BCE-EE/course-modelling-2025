"""
File: melt_demo.py

Author: Sasha D. Hafner 

Description:
    Demo of an ice melting model, including simple validation with measurements.
"""

# Python packages
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
import pandas as pd

# Our module
import ice_mods as im

# Let's get some measurements (these are real--I made them on my dining table some months ago!)
# Mass is in g
meas = pd.read_csv("meas_data/ice_meas.csv")
meas

# Get time in the right units.
meas["time_sec"] = meas["time_min"] * 60.

# And some for plotting
meas["time_hr"] = meas["time_min"] / 60.

# And ice ice in kg
meas["ice_kg_1"] = meas["ice_g_1"] / 1000.
meas["ice_kg_2"] = meas["ice_g_2"] / 1000.

# Validation 2. Get quantitative
# We need to have measurements and predictions at the same times in order to quantify model fit.
# The best approach to have a model function that returns specified times.
# We"ll change the original one.

reload(im)

pred01 = im.melt2(
    mass_0 = 0.027, 
    temp_air = 24, 
    h = 50, 
    times =  meas.time_sec
)

pred02 = im.melt2(
    mass_0 = 0.027, 
    temp_air = 24, 
    h = 75, 
    times =  meas.time_sec
)


pred01

# Plot comparison of course!
plt.close()
plt.plot(meas.time_hr, meas.ice_g_1, "k.")
plt.plot(pred01["t"] / 3600, 1000 * pred01["m"])
plt.plot(pred02["t"] / 3600, 1000 * pred02["m"])
plt.xlabel("Time (h)")
plt.ylabel("Ice mass (g)")
plt.savefig("plots/demo.png")

# Get sum of squared residuals
sum((meas.ice_g_1 - 1000 * pred01["m"])**2)
sum((meas.ice_g_1 - 1000 * pred02["m"])**2)
