"""
File: demo1.py
Authors: Frederik Dalby and Sasha Hafner

Description:
    Demo of the lagoon O2 reaction-transport model for mini-project 2.
"""

# Load modules
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

# Load user-defined model module
import O2dc_mods as oxm

# In case of edits to module, reload like this
#reload(oxm)

# See module code or run the help() command below for info on input parameters
#help(oxm.O2dc)

# Note that model code uses kg, m3, and s, but sometimes we want
# to set inputs or show results in different units, so we'll
# convert on the fly. We could use the conversion factor
# 86400 below for that.
sec2day = 60 * 60 * 24

# Two years of predictions
# dx is kind of large but that's OK for a demo
pred01 = oxm.O2dc(
    L =  0.1,               # m
    dx = 0.01,              # m
    k =  2E-5,               # m3/kg-d
    tmax = 2 * 365 * 86400, # 2 years
    nt = 100,
    O2_init = 0.01,         # completely aerobic to start with
    OM_init = 0.1,           # kg/m3 (100 mg/L) 
    O2_sat = 0.01,          # kg/m3 (10 mg/L)
    D = {                   # m2/s 
        "O2": 2.1E-9,
        "OM": 1.5E-9
    }
)

# Extract results and do some unit conversion
# O2 is O2 concentration, 2D array with position and time (kg/m3)
# Convert to mg/L
O2 = 1000 * pred01["O2"]
# OM is OM substrate concentration, 2D array with position and time (kg/m3)
# Convert to mg/L
OM = 1000 * pred01["OM"]
# Keep x position in m
x = pred01["x"]
# Convert time to days
days = pred01["t"]/60/60/24

# Take a look at the objects to be sure you understand the structure!

# Plot O2 vs. time
plt.close()
plt.plot(days, O2[0, :], label = f"{x[0]} m")
plt.plot(days, O2[round(len(x)/2), :], label = f"{x[round(len(x)/2)]} m")
plt.plot(days, O2[-1, :], label = f"{x[-1]} m")
plt.ylabel("Dissolved $\\mathrm{O}_2$ concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend(loc = 1)
plt.savefig("plots/O2_conc_demo.png")

# Plot OM vs. time
plt.close()
plt.plot(days, OM[0, :], label = f"{x[0]} m")
plt.plot(days, OM[round(len(x)/2), :], label = f"{x[round(len(x)/2)]} m")
plt.plot(days, OM[-1, :], label = f"{x[-1]} m")
plt.ylabel("OM concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend(loc = 1)
plt.savefig("plots/OM_conc_demo.png")

# Plot O2 vs. position (profiles)
plt.close()
plt.plot(O2[:, 0],  -x, label = round(days[0] ))
plt.plot(O2[:, 10], -x, label = round(days[10]))
plt.plot(O2[:, 50], -x, label = round(days[50]))
plt.plot(O2[:, 90], -x, label = round(days[90]))
plt.ylabel("Position (m)")
plt.xlabel("Dissolved $\\mathrm{O}_2$ concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.legend()
plt.savefig("plots/O2_profs_demo.png")

# And OM profiles
# Let"s use a loop this time to show a more efficient way
plt.close()
for i in (0, 10, 50, 90):
    plt.plot(OM[:, i], -x, label = f"{round(days[i])} d")
plt.ylabel("Position (m)")
plt.xlabel("OM concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.legend()
plt.savefig("plots/OM_profs_demo.png")

