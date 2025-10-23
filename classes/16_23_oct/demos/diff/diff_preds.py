"""
File: diff1D_demo.py 

Author: Sasha D. Hafner

Description:
    Demo and some verification of a 1D diffusion model.

"""

# Packages
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

# And our model functions
import diff_mod as dm

# reload() as needed (after editing)
reload(dm)

ppp = dm.diff1D2o(L = 0.1,
                  n = 5,
                  D = 4E-9,
                  bc = [100, 0],
                  ci = 0,
                  t_eval = np.linspace(0, 80*86400, 10))

ppp
ppp['ml'] - ppp['mr']
sum(ppp['c'][:,-1] * ppp['dx'])

plt.plot(res['x'], res['c'][:, 2])
plt.plot(res['x'], res['c'][:, 9])
plt.xlabel('Position (m)')
plt.ylabel('Concentration (g/m3)')
plt.savefig('example_profs.png')


