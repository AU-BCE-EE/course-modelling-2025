"""
File: aeration.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    An analytical model for water aeration.
"""

# Import modules
import numpy as np
import matplotlib.pyplot as plt

# Constants
# kLa (1/h)
kla = 20
# Saturation O2 concentration (g/m3)
csat = 10

# Times
dt = 0.01
maxt = 1
times = np.arange(0, maxt + dt, dt)

# Results array
conc_o2 = csat * (1 - np.exp(-kla * times))

plt.close()
plt.plot(times, conc_o2)
plt.savefig('aeration_analytical.png')
