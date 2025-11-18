"""
File: application.py
Authors: Sasha Hafner and Frederik Dalby

Description:
    Application of the lagoon O2 reaction-transport model for mini-project 2.
"""

# Load modules
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
import O2dc_mods as oxm

# From description
"""
## 4. Model application
Use your model to predict at least one of the following:
1. How long time it takes to degrade most (at least 90%) of the initial OM in an 10 cm deep lagoon, 
2. The minimum dissolved oxygen concentration in the lagoon with 10 cm wastewater and time it occurs after loading a new batch of wastewater, 
3. The effect of increasing dissolved oxygen diffusivity (what could that represent?), or
4. The effect of increased or decreased substrate degradation rate.
"""

# 1. How long time it takes to degrade most (at least 90%) of the initial OM in an 10 cm deep lagoon? 
# We'll try 1 year and use a larger dx than in some simulations to 
# speed up the run
pred01 = oxm.O2dc(
    L = 0.1,
    dx = 0.005,
    k = 1.2E-4, 
    tmax = 365 * 86400, 
    nt = 365,           # Daily output
    O2_init  =  0.010,  # Set O2 to saturation point (aerated)
    OM_init =  0.1,
    O2_sat   = 0.010,
    D = {
        "O2": 2.1E-9,
        "OM": 1.5E-9
    }
)

# We need to sum up OM in the water column for each time
# Can use the NumPy sum() *method* for arrays
OMtot = (pred01["OM"] * pred01["dx"]).sum(0)

# Relative change
OMrrem = 100 * (1 - OMtot / OMtot[0])
OMrrem

# Final value is 100%, so the run was long enough
# So let's find the time for 90%

# First graphical
days = pred01["t"] / 86400

plt.close()
plt.plot(days, OMrrem)
plt.ylabel("OM removal (%)")
plt.xlabel("Time after filling (d)")
plt.grid(True, which="both")
plt.savefig("plots/app_OM_rem.png")

# We can see somewhere between 100 and 150 days

# Here is a way to find the first value above 90%
ti90 = np.argmax(OMrrem > 90)
days[ti90]
# About 130 days

# 2. The minimum dissolved oxygen concentration in the lagoon with 10 cm wastewater and time it occurs after loading a new batch of wastewater, 

# Let's use the same results to start out
# We expect the minimum at the bottom, so we'll use that (not a bad idea to check though)
O2bot = 1000 * pred01["O2"][-1, :]

# Plot
plt.close()
plt.plot(days, O2bot)
plt.ylabel("Bottom $\\mathrm{O}_2$ concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.grid(True, which="both")
plt.savefig("plots/app_O2_bot.png")

# Looks like it is before 50 days
timinO2 = np.argmin(O2bot)
days[timinO2]

# 10.03 days

# 3. The effect of increasing dissolved oxygen diffusivity (what could that represent?), or

# We'll increase it and OM diffusivity by 10x
# This could represent some mixing, e.g., by wind or temperature-driven 
# buoyancy effects.
# In fact it is unrealistic to assume there is no mixing in an open lagoon!

pred02 = oxm.O2dc(
    L = 0.1,
    dx = 0.005,
    k = 1.2E-4, 
    tmax = 365 * 86400, 
    nt = 365,           
    O2_init  =  0.010, 
    OM_init =  0.1,
    O2_sat   = 0.010,
    D = {
        "O2": 10 * 2.1E-9,
        "OM": 10 * 1.5E-9
    }
)

# For a response, let's take bottom O2 again
O2bot01 = 1000 * pred01["O2"][-1, :]
O2bot02 = 1000 * pred02["O2"][-1, :]

# Plot
plt.close()
plt.plot(days, O2bot01, label = "Reference")
plt.plot(days, O2bot02, label = "10x D")
plt.ylabel("Bottom $\\mathrm{O}_2$ concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend()
plt.savefig("plots/app_O2_bot_mix.png")

# Does this result make sense?

# 4. The effect of increased or decreased substrate degradation rate.

# Let's increase the rate

pred03 = oxm.O2dc(
    L = 0.1,
    dx = 0.005,
    k = 3 * 1.2E-4, 
    tmax = 365 * 86400, 
    nt = 365,           
    O2_init  =  0.010, 
    OM_init =  0.1,
    O2_sat   = 0.010,
    D = {
        "O2": 2.1E-9,
        "OM": 1.5E-9
    }
)

# For a response, let's take bottom O2 again
O2bot01 = 1000 * pred01["O2"][-1, :]
O2bot03 = 1000 * pred03["O2"][-1, :]

# Plot
plt.close()
plt.plot(days, O2bot01, label = "Reference")
plt.plot(days, O2bot03, label = "3x reaction rate")
plt.ylabel("Bottom $\\mathrm{O}_2$ concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend()
plt.savefig("plots/app_O2_bot_fast.png")

# So bottom O2 drops to zero faster, but also rises faster
# Does that make sense?

