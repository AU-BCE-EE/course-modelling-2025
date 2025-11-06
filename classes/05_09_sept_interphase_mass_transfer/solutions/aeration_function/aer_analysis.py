"""
File: aeration.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    Application of some simple models for water aeration.
"""

# Import modules
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

# Import aeration model function from aeration_funcs.py script
import aer_mods as am

# Reload it after making changes to function code
reload(am)

# Set some times for output (h)
dt = 0.1
maxt = 2
times = np.arange(0, maxt + dt, dt)

# Call analytical and numerical model functions for comparison
pred_num1 = am.aer_num(kla = 5, csat = 10, c0 = 0, times = times)
pred_an1 =   am.aer_an(kla = 5, csat = 10, c0 = 0, times = times)
pred_num2 =   am.aer_cons_num(kla = 5, csat = 10, c0 = 0, cons = 0, times = times)

# Plot comparison
plt.close()
plt.plot(times, pred_num1, 'r-')
plt.plot(times, pred_an1, 'b:')
plt.plot(times, pred_an1, 'go')
plt.xlabel('Time (h)')
plt.ylabel('Predicted dissolved oxygen (mg/L)')
plt.savefig('aeration_comp1.png')

# Compare the two approaches when initial conc is not zero
pred_num2 = am.aer_num(kla = 5, csat = 10, c0 = 5, times = times)
pred_an2 =   am.aer_an(kla = 5, csat = 10, c0 = 5, times = times)

# Plot comparison
plt.close()
plt.plot(times, pred_num2, 'r-')
plt.plot(times, pred_an2, 'b:')
plt.xlabel('Time (h)')
plt.ylabel('Predicted dissolved oxygen (mg/L)')
plt.ylim(0, 11)
plt.savefig('aeration_comp2.png')

# Try adding some consumption (m/m3-h)
pred_cons1 = am.aer_cons_num(kla = 5, csat = 10, c0 = 0, cons = 10, times = times)
pred_cons2 = am.aer_cons_num(kla = 5, csat = 10, c0 = 0, cons = 50, times = times)
pred_cons3 = am.aer_cons_num(kla = 5, csat = 10, c0 = 0, cons = 75, times = times)

plt.close()
plt.plot(times, pred_cons1, 'r-', label = '10')
plt.plot(times, pred_cons2, 'b-', label = '50')
plt.plot(times, pred_cons3, 'g-', label = '75')
plt.ylim(-11, 11)
plt.xlabel('Time (h)')
plt.legend()
plt.ylabel('Predicted dissolved oxygen (mg/L)')
plt.savefig('aeration_consumption.png')
