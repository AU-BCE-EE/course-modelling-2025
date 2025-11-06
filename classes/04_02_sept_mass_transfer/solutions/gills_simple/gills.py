"""
File: gills.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    Some calculations on oxygen transfer flux through fish gills, based
    on a simple mass transfer coefficient approach.
"""

import numpy as np
import matplotlib.pyplot as plt

# Use an array for the two given L values (m)
L = np.array([20, 50]) * 1E-6
print(L)

# Set diffusivity (m2/s)
D = 2E-9

# Calculate associated mass transfer coefficients (m/s)
kc = D / L
print(kc)

# Now calculate the oxygen mass flux for these two conditions (g/m2-s)
# First we need delta concentration (g/m3 = mg/L)
dconc = 10 - 0
flux = kc * dconc
print(flux)

# So the maximum rate is 0.001 g/ms-s or 1 mg/m2-s
