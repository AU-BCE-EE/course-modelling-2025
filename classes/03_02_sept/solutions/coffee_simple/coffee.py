"""
File: coffee.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    A very simple model for a cup of coffee cooling off.
"""

# Import modules
import numpy as np
import matplotlib.pyplot as plt

# Times, up to 60 min (s)
times = np.arange(0, 61, 1) * 60
times

# Heat transfer coefficient (W/m2-K)
h = 25

# Area (m2)
A = 0.0258

# Initial condition (degrees C)
Tc0 = 80

# Ambient temperature
Tair = 20

# Coffee mass (g)
m = 300

# Specific heat of water (J/g-K)
cp = 4.2

# Solution
# First the constant that combines some variables and parameters
c = A * h / (cp * m)
# And the solution
Tc = (Tc0 - Tair) * np.exp(-c * times) + Tair

# Plot predictions
plt.close()
plt.plot(times / 60, Tc)
plt.xlabel('Time (min)')
plt.ylabel('Temperature $(^\circ~\mathregular{C})$')
plt.savefig('coffee_temp.png')

# I don't have measurements, but that does not look very likely!
# Why might the convection heat transfer coefficient in fact be much higher?
# Heat transfer coefficient (W/m2-K)
h = 100

# Solution
# First the constant that combines some variables and parameters
c = A * h / (cp * m)
# And the solution
Tc = (Tc0 - Tair) * np.exp(-c * times) + Tair

# Plot predictions
plt.close()
plt.plot(times / 60, Tc)
plt.xlabel('Time (min)')
plt.ylabel('Temperature $(^\circ~\mathregular{C})$')
plt.savefig('coffee_temp2.png')


