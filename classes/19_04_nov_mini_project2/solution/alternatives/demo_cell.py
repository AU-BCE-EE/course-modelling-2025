"""
Demo of O2 diffusion model
"""

import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

import O2dc_cell_mods as oxm

reload(oxm)

pred01 = oxm.O2dcc(
    L = 0.05,
    N = 40,
    k = 1E-3,
    tmax = 10 * 86400,
    nt = 20,
    S_init = 1. 
)

pred01["O2"]
pred01["x"]
pred01["dx"]

# Plot profiles
plt.close()
plt.plot(pred01['O2'][:, 0], -pred01['x'])
plt.plot(pred01['O2'][:, 1], -pred01['x'])
plt.plot(pred01['O2'][:, 5], -pred01['x'])
plt.plot(pred01['O2'][:, 19], -pred01['x'])
plt.ylabel('Position (m)')
plt.xlabel('Concentration (kg/m3)')
plt.savefig('plots/O2_profs_cell.png')

plt.close()
plt.plot(pred01['S'][:, 0], -pred01['x'])
plt.plot(pred01['S'][:, 1], -pred01['x'])
plt.plot(pred01['S'][:, 5], -pred01['x'])
plt.plot(pred01['S'][:, 19], -pred01['x'])
plt.ylabel('Position (m)')
plt.xlabel('Concentration (kg/m3)')
plt.savefig('plots/S_profs_cell.png')
