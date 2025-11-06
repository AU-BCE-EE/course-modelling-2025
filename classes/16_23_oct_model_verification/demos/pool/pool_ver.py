"""
File: pool_ver.py

Author: Sasha D. Hafner

Description: 
    Verification of the swimming pool heat transfer model.
"""

# Packages
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

# Get out pool model functions (loading a module here)
# This will not load a new version!
import pool_mods as pm

# Use as needed (reload(pm) if module code is changed)
reload(pm)

# Set dimensions (all distances m, all areas m^2).
# Assume pool is 10 x 4 x 2 m.
length = 10
width = 4
depth = 2
a_top = length * width
a_wall = 2 * (length + width) * depth + a_top

# And a demo model call
pred01 = pm.dynmod(a_top = a_top,
                   a_wall = a_wall,
                   depth = depth,
                   q_sol = 0,
                   u_top = 100,
                   u_wall = 3,
                   temp_air = 10,
                   temp_sub = 10,
                   flow_renew = 0,
                   temp_renew = 0,
                   temp_init = 30,
                   times = np.arange(0, 12 * 3600 + 3600, 3600)
)

# Check results
pred01
pred01['temp']

# And 
plt.plot(pred01['t'] / 3600, pred01['temp'])
plt.xlabel('Time (h)')
plt.ylabel('Pool temperature (deg. C)')
plt.savefig('pred01.png')

# Conceptual and unit check (see md file)
# . . . .

# Now some model calls

# 1. Think about steady-state
# Should there be a steady state condition?
# Sure! 
# A. With the sun shining, the pool water will warm above ambient temperature 
# but eventually reach a steady-state where it . . .  

# Let's add 200 W/m2 of sun, keep environment at 10, and see
pred02 = pm.dynmod(a_top = a_top,
                   a_wall = a_wall,
                   depth = depth,
                   q_sol = 200,
                   u_top = 100,
                   u_wall = 3,
                   temp_air = 10,
                   temp_sub = 10,
                   flow_renew = 0,
                   temp_renew = 0,
                   temp_init = 10,
                   times = np.arange(0, 12 * 3600 + 3600, 3600)
)

pred02

# Run it for a long time
# Is this a realistic simulation, by the way?
pred03 = pm.dynmod(a_top = a_top,
                   a_wall = a_wall,
                   depth = depth,
                   q_sol = 200,
                   u_top = 100,
                   u_wall = 3,
                   temp_air = 10,
                   temp_sub = 10,
                   flow_renew = 0,
                   temp_renew = 0,
                   temp_init = 10,
                   times = np.arange(0, 30 * 86400 + 86400, 86400)
)

pred03['temp']

plt.close()
plt.plot(pred03['t'] / 86400, pred03['temp'])
plt.xlabel('Time (d)')
plt.ylabel('Pool temperature (deg. C)')
plt.savefig('pred03.png')

# As expected?
# Higher or lower than ambient?
# What about the oscillations?

# Does it match steady state model?
pm.ssmod(a_top = a_top,
         a_wall = a_wall,
         depth = depth,
         q_sol = 200,
         u_top = 100,
         u_wall = 3,
         temp_air = 10,
         temp_sub = 10,
         flow_renew = 0,
         temp_renew = 0
)

pred03['temp'][10:]

# Hmmm. . . does it?
# Is there an error in the model?

# Try renewal
# If we are interested in steady state, we might just return a few times
pm.dynmod(a_top = a_top,
          a_wall = a_wall,
          depth = depth,
          q_sol = 0,
          u_top = 100,
          u_wall = 3,
          temp_air = 10,
          temp_sub = 10,
          flow_renew = 0.1,
          temp_renew = 30,
          temp_init = 10,
          times = [0, 3600, 86400, 10*86400] 
)

# Big problem!
# We get massively negative temperature
# Let's dig into this, first with some more model calls
# Think about it . . . 
# Try smaller delta T and shorter time to slow down heat transfer and time, in a sense

pm.dynmod(a_top = a_top,
          a_wall = a_wall,
          depth = depth,
          q_sol = 0,
          u_top = 100,
          u_wall = 3,
          temp_air = 10,
          temp_sub = 10,
          flow_renew = 0.1,
          temp_renew = 10.1,
          temp_init = 10,
          times = np.arange(0, 101)
)

# Adjust the time a bit. . .
# What does that tell us?

# Try breakpoint() to see what is happening
# Edit module and . . .
reload(pm)

pm.dynmod(a_top = a_top,
          a_wall = a_wall,
          depth = depth,
          q_sol = 0,
          u_top = 100,
          u_wall = 3,
          temp_air = 10,
          temp_sub = 10,
          flow_renew = 0.1,
          temp_renew = 10.1,
          temp_init = 10,
          times = np.arange(0, 101)
)

# Check:
Q_renew
# Negative or positive?
temp_pool
temp_renew
# See it?

# See module code in rates()
# Q_renew = cp * dens * flow_renew * (temp_pool - temp_renew) # Net energy coming in from renewal water

# Possible checks
# * Correct steady-state predictions with solar radiation and other changes to inputs (possibly changed independently or stepwise)
# * Correct qualitative effects of changes to inputs (more or less radiation, higher or lower substrate temperature or resistance)

# We can check implementation of constitutive equation quantitatively with some careful calls and analysis of results
# breakpoint() can be used to check for object (variable) values during evlauation of rates() function

# For a quantitative check of energy balance, we can add cumulative heat transfer as state variables
# Let's try this new version

reload(pm)

pm.dynmod_pp(a_top = a_top,
             a_wall = a_wall,
             depth = depth,
             q_sol = 0,
             u_top = 100,
             u_wall = 3,
             temp_air = 10,
             temp_sub = 10,
             flow_renew = 0.1,
             temp_renew = 10.1,
             temp_init = 10,
             times = np.arange(0, 10)
)

# See huge negative h_renew (J).
# Wrong sign!
# And a flow of 0.1 m3/s (100 L/s) is probably high for a pool that is 10 x 4 x 2 = 80 m3

# Let's try to fix the error

# And do you see how these cumulative transport state variables can be useful and interesting?
# Should we plot some for different scenarios?
