"""
File: aeration.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    A numerical model for water aeration.
"""

# Import modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
# kLa (1/h)
kla = 20
# Saturation O2 concentration (g/m3)
csat = 10

# Forward Euler's method with fixed time step

# Times
dt = 0.01
maxt = 1
times = np.arange(0, maxt + dt, dt)

# Results array
conc_o2 = np.zeros_like(times)
conc_o2[0] = 0

for i in range(1, len(conc_o2)):
    conc_o2[i] = conc_o2[i - 1] + kla * (csat - conc_o2[i - 1]) * dt

plt.close()
plt.plot(times, conc_o2)
plt.savefig('aeration_num1.png')

# Note that the method fails with a much higher time step

# Try a more sophisticated approach--solve_ivp()
def rates(t, c):
    return kla * (csat - c)

res = solve_ivp(rates, t_span = (0, 1), y0 = [0], t_eval = times)

plt.close()
plt.plot(times, res.y[0, :])
plt.savefig('aeration_num2.png')


