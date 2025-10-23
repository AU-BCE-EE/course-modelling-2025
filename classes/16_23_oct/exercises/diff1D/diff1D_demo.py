"""
File: diff1D_demo.py 

Author: Sasha D. Hafner

Description:
    Demo of a 1D diffusion model.

"""

# Packages
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

# And our model functions
import diff_mod as dm

# reload() as needed (after editing)
reload(dm)

pred = dm.diff1D(L = 0.1,
                 n = 20,
                 D = 4E-9,
                 bc = [100, 0],
                 ci = 0,
                 t_eval = np.linspace(0, 86400, 10))

# View output
pred
# Tip: It can be easier to understand and view output if you reduce the number of layers/cells to e.g., 5
# You could also reduce the number of times

# Plot profiles
plt.close()
plt.plot(pred['x'], pred['c'][:, 1])
plt.plot(pred['x'], pred['c'][:, 2])
plt.plot(pred['x'], pred['c'][:, 5])
plt.plot(pred['x'], pred['c'][:, 9])
plt.xlabel('Position (m)')
plt.ylabel('Concentration (g/m3)')
plt.savefig('conc_profs.png')



