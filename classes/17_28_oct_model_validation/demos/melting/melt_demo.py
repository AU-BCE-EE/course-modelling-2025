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

# Use as needed
reload(im)

# Set some constants.
h = 50          # W/m2-K
temp_air = 20   # deg. C

# Initial ice mass
m0 = 1.         # kg

# Run the model by calling the model function.

pred01 = im.melt(
    mass_0 = m0, 
    temp_air = temp_air, 
    h = 50, 
    t_range = [0, 10*3600], 
    t_step = 600
)

pred01

# Plot results.
plt.plot(pred01['t'] / 3600, pred01['m'])
plt.xlabel('Time (h)')
plt.ylabel('Ice mass (kg)')
plt.savefig('figs/pred01.png')

# So 1 kg would last more than 10 hours, if the model is correct
# Could be!

# Let's get some measurements (these are reall--I made them on my dining table some months ago!)
# Mass is in g
meas = pd.read_csv('data/ice_meas.csv')
meas

# Get time in the right units.
meas['time_sec'] = meas['time_min'] * 60.

# And some for plotting
meas['time_hr'] = meas['time_min'] / 60.

# And ice ice in kg
meas['ice_kg_1'] = meas['ice_g_1'] / 1000.
meas['ice_kg_2'] = meas['ice_g_2'] / 1000.

# Plot measurements

```{python}
plt.close()
plt.plot(meas.time_hr, meas.ice_kg_1, 'r.')
plt.plot(meas.time_hr, meas.ice_kg_2, 'b.')
plt.xlabel('Time (h)')
plt.ylabel('Ice mass (kg)')
plt.savefig('figs/meas.png')
```

# Validation 1: Compare the model to measurements graphically

pred02 = im.melt(
    mass_0 = 0.027, 
    temp_air = 24, 
    h = 50, 
    t_range = (0, 200 * 60), 
    t_step =  600
)

pred02

plt.plot()

# Validation 2. Get quantitative
# We need to have measurements and predictions at the same times in order to quantify model fit.
# The best approach to have a model function that returns specified times.
# We'll change the original one.

reload(im)

pred03 = im.melt2(
    mass_0 = 0.027, 
    temp_air = 24, 
    h = 50, 
    times =  meas.time_sec
)

pred03

# Plot comparison of course!

# And plot residuals . . .

# And fit statistics
import mod_fit as mf

mf.nse(meas.ice_kg_1, pred03['m'])
mf.mae(meas.ice_kg_1, pred03['m'])
1000 * mf.mae(meas.ice_kg_1, pred03['m'])
...

# How about comparison to the mean of measurements?
# Or two different comparisons

meas . .  .  ( meas.ice_kg_1 + meas.ice_kg_2

# Let's try a different convection heat transfer coefficient value.
# Why might a larger value be appropriate?

pred04

# It is good practice to use data frames.
# Let's write a new model function that returns a data frame.

reload(im)

# We can now easily merge these results with measurements.

pred05

meas
eval = pd.merge(meas, pred04, left_on = 'time_sec', right_on = 'time')
eval

mf.nse(eval.ice_kg_1, eval...)
