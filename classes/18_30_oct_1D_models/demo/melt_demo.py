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
plt.close()
plt.plot(pred01['t'] / 3600, pred01['m'])
plt.xlabel('Time (h)')
plt.ylabel('Ice mass (kg)')
plt.savefig('figs/pred01.png')

# So 1 kg would last more than 10 hours, if the model is correct
# Could be!

# Let's get some measurements (these are real--I made them on my dining table some months ago!)
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

plt.close()
plt.plot(meas.time_hr, meas.ice_kg_1, 'r.')
plt.plot(meas.time_hr, meas.ice_kg_2, 'b.')
plt.xlabel('Time (h)')
plt.ylabel('Ice mass (kg)')
plt.savefig('figs/meas.png')

# Validation 1: Compare the model to measurements graphically

pred02 = im.melt(
    mass_0 = 0.027, 
    temp_air = 24, 
    h = 50, 
    t_range = (0, 200 * 60), 
    t_step =  600
)

pred02

# Make a plot. . . 
plt.close()
plt.plot(meas.time_hr, meas.ice_kg_1, 'r.')
plt.plot(meas.time_hr, meas.ice_kg_2, 'b.')
plt.plot(pred02['t'] / 3600, pred02['m'])
plt.xlabel('Time (h)')
plt.ylabel('Ice mass (kg)')
plt.savefig('figs/comp.png')

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
plt.close()
plt.plot(meas.time_hr, meas.ice_kg_1, 'r.')
plt.plot(meas.time_hr, meas.ice_kg_2, 'b.')
plt.plot(pred03['t'] / 3600, pred03['m'])
plt.xlabel('Time (h)')
plt.ylabel('Ice mass (kg)')
plt.savefig('figs/comp2.png')

# And fit statistics
import mod_fit as mf

1000 * mf.mbe(meas.ice_kg_1, pred03['m'])
1000 * mf.mae(meas.ice_kg_1, pred03['m'])

# How about comparison to the mean of measurements?
meas['ice_mean_kg'] = (meas['ice_kg_1'] + meas['ice_kg_2']) / 2

plt.close()
plt.plot(meas.time_hr, meas.ice_mean_kg, 'r.')
plt.plot(pred03['t'] / 3600, pred03['m'])
plt.xlabel('Time (h)')
plt.ylabel('Ice mass (kg)')
plt.savefig('figs/comp3.png')

1000 * mf.mbe(meas.ice_mean_kg, pred03['m'])
1000 * mf.mae(meas.ice_mean_kg, pred03['m'])

# Let's try a different convection heat transfer coefficient value.
# Why might a larger value be appropriate?

pred04 = im.melt2(
    mass_0 = 0.027, 
    temp_air = 24, 
    h = 100, 
    times =  meas.time_sec
)

pred04

plt.close()
plt.plot(meas.time_hr, meas.ice_mean_kg, 'r.')
plt.plot(pred03['t'] / 3600, pred03['m'])
plt.plot(pred04['t'] / 3600, pred04['m'])
plt.xlabel('Time (h)')
plt.ylabel('Ice mass (kg)')
plt.savefig('figs/comp4.png')

# It is good practice to use data frames.
# Let's write a new model function that returns a data frame.
reload(im)

pred05 = im.melt3(
    mass_0 = 0.02752, 
    temp_air = 24, 
    h = 100, 
    times =  meas.time_sec
)

pred05

# We can now easily merge these results with measurements.
eval = pd.merge(meas, pred05, on = 'time_sec')
eval

# We should use a clearer name
eval.rename(columns = {'mass_kg': 'ice_mod_kg'}, inplace = True)

# Calculate residuals or model error for each time
eval['resid'] = eval['ice_mod_kg'] - eval['ice_mean_kg']

# And plot
plt.close()
plt.plot(eval.time_hr, eval.resid, 'r.')
plt.xlabel('Time (h)')
plt.ylabel('Ice mass (kg)')
plt.savefig('figs/resids.png')

# How about shifting the time?
plt.close()
plt.plot(eval.time_hr - 0.17, meas.ice_mean_kg, 'r.', label = 'Measurements')
plt.plot(eval.time_hr, eval.ice_mod_kg, label = 'Model, h = 100')
plt.xlabel('Time (h)')
plt.ylabel('Ice mass (kg)')
plt.legend()
plt.savefig('figs/comp5.png')

# Let's make predictions for some more values of h and merge them all in
pred_h50 = im.melt3(
    mass_0 = 0.02752, 
    temp_air = 24, 
    h = 50, 
    times =  meas.time_sec
)

pred_h100 = im.melt3(
    mass_0 = 0.02752, 
    temp_air = 24, 
    h = 100, 
    times =  meas.time_sec
)

pred_h120 = im.melt3(
    mass_0 = 0.02752, 
    temp_air = 24, 
    h = 120, 
    times =  meas.time_sec
)

pred_h200 = im.melt3(
    mass_0 = 0.02752, 
    temp_air = 24, 
    h = 200, 
    times =  meas.time_sec
)

# Merge and rename as we go
eval = pd.merge(meas, pred_h50, on = 'time_sec')
eval.rename(columns = {'mass_kg': 'ice_mod_kg_h50'}, inplace = True)

eval = pd.merge(eval, pred_h100, on = 'time_sec')
eval.rename(columns = {'mass_kg': 'ice_mod_kg_h100'}, inplace = True)

eval = pd.merge(eval, pred_h120, on = 'time_sec')
eval.rename(columns = {'mass_kg': 'ice_mod_kg_h120'}, inplace = True)

eval = pd.merge(eval, pred_h200, on = 'time_sec')
eval.rename(columns = {'mass_kg': 'ice_mod_kg_h200'}, inplace = True)


plt.close()
plt.plot(eval.time_hr - 0.17, eval.ice_mean_kg, 'r.', label = 'Measured')
plt.plot(eval.time_hr, eval.ice_mod_kg_h50, label = 'model, h = 50')
plt.plot(eval.time_hr, eval.ice_mod_kg_h100, label = 'model, h = 100')
plt.plot(eval.time_hr, eval.ice_mod_kg_h120, label = 'model, h = 120')
plt.plot(eval.time_hr, eval.ice_mod_kg_h200, label = 'model, h = 200')
plt.xlabel('Time (h)')
plt.ylabel('Ice mass (kg)')
plt.legend()
plt.savefig('figs/comp6.png')

1000 * mf.mbe(eval.ice_mean_kg, eval.ice_mod_kg_h120)
1000 * mf.mae(eval.ice_mean_kg, eval.ice_mod_kg_h120)

