"""
Create fake measurement data for mini-project 2.
"""

import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

import O2dc_mods as oxm

# Get concentration at bottom of 0.1 m deep lagoon
# With 2x ref D
pred01 = oxm.O2dc(
    L = 0.1,
    dx = 0.002,
    k = 1E-4,
    tmax = 60 * 86400,
    nt = 60,
    O2_init  =  0.01,
    S_init =  0.02,
    O2_sat   = 0.01,
    D = {
        "O2": 2 * 2.1E-9,
        "S": 2 * 1.5E-9
    }
)

# With reference D
pred02 = oxm.O2dc(
    L = 0.1,
    dx = 0.002,
    k = 1E-4,
    tmax = 60 * 86400,
    nt = 30,
    O2_init  =  0.01,
    S_init =  0.02,
    O2_sat   = 0.01,
    D = {
        "O2": 2.1E-9,
        "S": 1.5E-9
    }
)


# Extract data and convert units (d and mg/L)
O2 = pred01["O2"]
days = pred01["t"]/60/60/24
bottom_O2 = 1000 * O2[-1,:]

# adding noise to data
r_error = 0.05
a_error = 0.05
bottom_O2_data = (bottom_O2 * (1 + np.random.normal(0, r_error, size = bottom_O2.shape)) + (np.random.normal(0, a_error, size = bottom_O2.shape)))

import pandas as pd
data = pd.DataFrame({
    "day": days,
    "bottom_O2_mg_L": bottom_O2_data
})

# Export data
data.to_csv("data/meas_O2.csv")

# Plot
plt.close()
plt.plot(data.day, data.bottom_O2_mg_L, 'ro')
plt.plot(pred02['t']/86400, 1000 * pred02['O2'][-1, :], 'b-')
plt.ylabel('conc (mg/L)')
plt.xlabel('time, days')
plt.legend(loc = 1)
plt.savefig('plots/O2_conc_meas.png')


# S profiles
plt.close()
plt.plot(pred02['S'][:, 0], -pred02['x'])
plt.plot(pred02['S'][:, 10], -pred02['x'])
plt.plot(pred02['S'][:, 50], -pred02['x'])
plt.ylabel('Position (m)')
plt.xlabel('Concentration (kg/m3)')
plt.savefig('plots/S_profs_make_data.png')

pred02['S'].shape





