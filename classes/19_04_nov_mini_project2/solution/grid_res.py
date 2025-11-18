"""
File: grid_res.py
Author: Sasha Hafner

Description:
   A check of grid size effect in 1D reaction-transport model.
"""

import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
import O2dc_mods as oxm

# Start with dx = 0.01 m (1/10th of depth)
dx = 0.01
pred01 = oxm.O2dc(
    L =  0.1,
    dx = dx,
    k = 1E-3,
    tmax = 5 * 86400,
    nt = 2,
    O2_init = 0.01, 
    OM_init = 0.02, 
    O2_sat = 0.01, 
    D = {
        "O2": 2.1E-9,
        "OM": 1.5E-9
    }
)

# Check total OM in mg/m2 as response (mg just to have larger numbers)
OMrem = 1E6 * sum((pred01["OM"][:, 0] - pred01["OM"][:, -1]) * pred01['dx'])
OMrem
OMinit = 1E6 * sum(pred01["OM"][:, 0] * pred01['dx'])
OMinit

# Let's try other dx values
# We could copy/paste the code above for several dx values, 
# but it is more efficient to set this up in a loop.

# Initial dx
dx_init = 0.01

# Number of times to divide dx by 2
nd = 5 + 1

# Empty arrays for results
res = np.zeros(nd)
dxl = np.zeros(nd)

dx = dx_init
for i in range(0, nd, 1):
    pred = oxm.O2dc(
        L =  0.1,
        dx = dx,
        k = 1E-3,
        tmax = 5 * 86400,
        nt = 2,
        O2_init = 0.01, 
        OM_init = 0.02, 
        O2_sat = 0.01, 
        D = {
            "O2": 2.1E-9,
            "OM": 1.5E-9
        }
    )

    # Get total OM
    OMf = pred["OM"][:, -1]
    OMi = pred["OM"][:, 0]
    res[i] = 1E6 * sum((OMi - OMf) * pred['dx'])

    # Store dx
    dxl[i] = dx

    # Halve dx
    dx = dx / 2.

    print(i)


# Take a look
dxl
res

# Let's calculate relative difference from highest resolution
rel = 100 * np.abs(1 - res / res[-1])
# Or
#rel = 100 * np.abs((res - res[-1]) / res[-1])

# Absolute value
plt.close()
plt.semilogx(dxl, res, "ro")
plt.gca().invert_xaxis()
plt.ylabel("5 day OM removal ($\\mathrm{mg}~\\mathrm{m}^{-2}$)")
plt.xlabel("dx (m)")
plt.grid(True, which="both")
plt.savefig("plots/grid_res_abs.png")

# Relative difference from finest
plt.close()
plt.semilogx(dxl, rel, "ro")
plt.gca().invert_xaxis()
plt.ylabel("Relative difference in 5 day OM removal (% ref.)")
plt.xlabel("dx (m)")
plt.grid(True, which="both")
plt.savefig("plots/grid_res_rel.png")





