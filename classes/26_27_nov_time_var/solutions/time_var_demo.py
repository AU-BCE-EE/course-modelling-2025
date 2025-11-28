"""
File: demo.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    Solution to time-variable parameter exercise.
"""

# Packages/modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import O2dc_mods as oxm

from importlib import reload

reload(oxm)

# Make some fake k data with a 24 hour cycle
# There are different ways to do this
k_dat = pd.DataFrame(
    {
        "time": 86400 * np.linspace(0, 60, 120),
        "k": 60 * [1E-4, 1E-5],
    }
)

k_dat

# Original model
pred01 = oxm.O2dc(
    L= 1,
    dx=0.01,
    k=5E-5,
    tmax=5 * 86400,
    nt=1000,
    O2_init=0.008,
    OM_init=0.01,
    O2_sat= 0.01,
    D={
        "O2": 2E-9,
        "OM": 2E-9
    }
)

# And time-variable
# We'll could use cubic for a smooth curve
# Try it, and see the issue with the ends
# Do you have an idea for fixing it?

pred02 = oxm.O2dcv(
    L= 1,
    dx=0.01,
    k_dat=k_dat,
    k_kind="linear",
    tmax=5 * 86400,
    nt=1000,
    O2_init=0.008,
    OM_init=0.01,
    O2_sat= 0.01,
    D={
        "O2": 2E-9,
        "OM": 2E-9
    }
)

# Extract results and do some unit conversion
# Middle OM
# Convert to mg/L and days
OM_mid_c = 1000 * pred01["OM"][51, :]
days_c = pred01["t"]/60/60/24
OM_mid_v = 1000 * pred02["OM"][51, :]
days_v = pred02["t"]/60/60/24
k_v = pred02["k"]

# Plot OM
plt.close()
plt.plot(days_c, OM_mid_c, label="Constant k")
plt.plot(days_v, OM_mid_v, label="Variable k")
plt.ylabel("Middle OM concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend()
plt.savefig("plots/OM_conc.png")

# And k
plt.close()
plt.plot(days_v, k_v)
plt.ylabel("Rate constant $k$ ($\\mathrm{m}^3~\\mathrm{kg}^{-1}~\\mathrm{s}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.savefig("plots/k_v.png")

# What happens for longer times?
# Note an important difference despite constnat k = average of time-variable extremes
