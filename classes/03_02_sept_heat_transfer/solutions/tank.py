"""
File: tank.py
Author: Sasha D. Hafner
Course: Modelling 2025
Description:
    Implementation of a simple model of a water tank draining water over time.
"""

# Packages
import numpy as np
import matplotlib.pyplot as plt

# Let's use NumPy arrays and vectorized calculations to calculate water volume at different times
# First we need the constants

# Rate constant c (1/min)
c = 0.01

# Initial volume (m3)
v0 = 10

# Times for the solution (min, 10 h total)
times = np.arange(0, 10 * 60 + 1, 1)

# And finally, the solution
v = v0 * np.exp(-c * times)

# Plot results
plt.close()
plt.plot(times, v)
plt.xlabel('Time (min)')
plt.ylabel('Tank water $(\mathregular{m}^3)$')
plt.savefig('tank.png')

