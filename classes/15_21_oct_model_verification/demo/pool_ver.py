"""
Verification of pool model.
Author: Sasha D. Hafner
"""

import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

import pool_mods as pm

# Use as needed (if module code is changed)
#reload(pm)

# Set areas (all m^2).
# Assume pool is 10 x 4 x 2 m.
length = 10
width = 4
depth = 2
a_top = length * width
a_wall = 2 * (length + width) * depth + a_top

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

pred01

plt.plot(pred01.t / 3600, pred01.y[0, :])
plt.xlabel('Time (h)')
plt.ylabel('Pool temperature (deg. C)')
plt.savefig('pred01.png')

# Conceptual and unit check (see md file)

# Now some model calls

# 1. Is there a steady state?
# Set temp_init to 10 and see
pred02 = pm.dynmod(a_top = a_top,
                   a_wall = a_wall,
                   depth = depth,
                   q_sol = 0,
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

# As expected?

# Does it match steady state model?
pm.ssmod(a_top = a_top,
         a_wall = a_wall,
         depth = depth,
         q_sol = 0,
         u_top = 100,
         u_wall = 3,
         temp_air = 10,
         temp_sub = 10,
         flow_renew = 0,
         temp_renew = 0
)

# Well. . . that is obvious!

# How about for other initial temperatures?

#pred03 = 

# Let's check other cases, where steady state temperature is not obvious.

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
          temp_renew = 0,
          temp_init = 10,
          times = [0, 3600, 86400, 10*86400] 
)

# Big problem!
# Try delta T = 0
pm.dynmod(a_top = a_top,
          a_wall = a_wall,
          depth = depth,
          q_sol = 0,
          u_top = 100,
          u_wall = 3,
          temp_air = 10,
          temp_sub = 10,
          flow_renew = 0.1,
          temp_renew = 10,
          temp_init = 10,
          times = [0, 3600, 86400, 10*86400] 
)

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
          temp_renew = 20,
          temp_init = 10,
          times = [0, 3600, 86400, 10*86400] 
)

# Check:
Q_renew
temp_pool
temp_renew

# See module code in rates()
# Q_renew = cp * dens * flow_renew * (temp_pool - temp_renew) # Net energy coming in from renewal water

# Possible checks
# * Correct steady-state predictions with solar radiation and other changes to inputs (possibly changed independently or stepwise)
# * Correct qualitative effects of changes to inputs (more or less radiation, higher or lower substrate temperature or resistance)

# We can check implementation of constitutive equation quantitatively with some careful calls and analysis of results
# breakpoint() can be used to check for object (variable) values during evlauation of rates() function
# For a quantitative check of energy balance, we can add cumulative heat transfer as state variables


