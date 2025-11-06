"""
File: diff1D_demo.py 

Author: Sasha D. Hafner

Class: Modelling 2025

Description:
    Demo of a 1D diffusion model.

"""

# Packages
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

# And our model functions
import diff_mods as dm

# reload() as needed (after editing module code)
reload(dm)

# Predictions for a 0.2 m column with 20 layers and a diffusivity of 2E-9 m2/s
# 100 kg/m3 salt on left side, none on right
# Over 10 days
pred = dm.diff1D(L = 0.2,
                 n = 20,
                 D = 2.1E-9,
                 bc = [100, 0],
                 ci = 0,
                 t_eval = np.linspace(0, 10 * 86400, 10))

# View output
pred
# Tip: It can be easier to understand and view output if you reduce the number of layers/cells to e.g., 5
# You could also reduce the number of times
# But while exploring the model function it is helpful if they do not have the same value (do you see why?)

# Concentrations (kg/m3) (2D array)
# All positions and times
pred['c']

# All positions, for final time only
pred['c'][:, -1]

# Middle (nearly) layer, all times
pred['c'][10, :]

# Layer thickness (m)
pred['dx']

# Cumulative mass transfer (kg/m2)
pred['ml']
pred['mr']

# Plot profiles
plt.close()
plt.plot(pred['x'], pred['c'][:, 0])
plt.plot(pred['x'], pred['c'][:, 1])
plt.plot(pred['x'], pred['c'][:, 2])
plt.plot(pred['x'], pred['c'][:, 5])
plt.plot(pred['x'], pred['c'][:, 9])
plt.xlabel('Position (m)')
plt.ylabel('Concentration (kg/m3)')
plt.savefig('conc_profs.png')



