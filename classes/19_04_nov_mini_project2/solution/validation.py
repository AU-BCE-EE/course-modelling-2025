"""
File: validation.py
Authors: Frederik Dalby and Sasha Hafner

Description:
    Validation of the lagoon O2 reaction-transport model for mini-project 2.
"""

# Packages/modules
# Include pandas now for reading from csv as DataFrame
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
import O2dc_mods as oxm
import pandas as pd
from importlib import reload

reload(oxm)

# Get measurements
meas = pd.read_csv('data/meas_O2.csv')

# Inspect
meas

# Run model for 60 days, like measurements
# Note input parameters set to info from project description
# Note smaller dx (see grid_res.py script)
pred01 = oxm.O2dc(
    L =  0.1,               # m
    dx = 0.001,             # m
    k =  1E-4,              # m3/kg-d
    tmax = 60 * 86400,      # 60 d
    nt = 100,
    O2_init = 0.01,         # completely aerobic to start with
    OM_init = 0.02,         # kg/m3 (20 mg/L) 
    O2_sat =  0.01,         # kg/m3 (10 mg/L)
    D = {                   # m2/s 
        "O2": 2.1E-9,
        "OM": 1.5E-9
    }
)

# Extract results and do some unit conversion
# Convert to mg/L
O2 = 1000 * pred01["O2"]
# Convert time to days
days = pred01["t"]/60/60/24

# Plot measurements (bottom node) and model
plt.close()
plt.plot(days, O2[-1,:], label = "Model")
plt.plot(meas.day, meas.bottom_O2_mg_L, "ro", label = 'Measurements')
plt.ylabel("Bottom $\\mathrm{O}_2$ concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend(loc = 1)
plt.savefig("plots/O2_conc_val_1.png")

# Take a look at the plot
# What do you think about model fit?

# For a quantitative assessment of fit, we need to have model and 
# measurement times aligned
days
meas.day

# Measurement time is a bit odd
meas.day.values[1:] - meas.day.values[:-1]

# It looks like the step size was meant to be 1 d exactly, but 
# someone made a mistake in creating the spacing!
# But as long as spacing is regular, we can use this model function
# (although we'll have to round below).
# For irregular spacing, we would have to change the model function.
# That is actually a better approach.

pred02 = oxm.O2dc(
    L =  0.1,               # m
    dx = 0.001,             # m
    k =  1E-4,              # m3/kg-d
    tmax = 60 * 86400,      # 60 d
    nt = 60,
    O2_init = 0.01,         # completely aerobic to start with
    OM_init = 0.02,         # kg/m3 (20 mg/L) 
    O2_sat =  0.01,         # kg/m3 (10 mg/L)
    D = {                   # m2/s 
        "O2": 2.1E-9,
        "OM": 1.5E-9
    }
)

pred02["t"] / 86400

# It looks like times are the same in the model output and measurement 
# DataFrame, so we could do this:

dat = meas.copy()
dat["O2_mod"] = 1000 * pred02["O2"][-1, :]
dat.head()
dat

# But it is safer to put the model output (O2 *and time*) in a DataFrame and merge
# Do you see why?

mod = pd.DataFrame({"day": pred02["t"] / 86400, "O2_mod": 1000 * pred02["O2"][-1, :]})
meas.day
mod.day

# And to merge, we should round the day columns first, to make sure we 
# don't drop any because of differences way out to the right.
# Note: a better approach would be to have our model function 
# accept specific times, which we could then get from the meas
# DataFrame.

meas["day"] = np.round(meas["day"], 3)
mod["day"] = np.round(mod["day"], 3)
meas.head()
mod.head()

dat = pd.merge(meas, mod, on = "day")
dat.head()
dat.tail()

# We can calculate mean absolute error (MAE) and mean bias error 
# (MBE) in a single line
MAE = np.mean(np.abs(dat.O2_mod - dat.bottom_O2_mg_L))
MBE = np.mean(dat.O2_mod - dat.bottom_O2_mg_L)
MAE
MBE
# Or import the modules from class and use the functions there

# Results show a tendency to underpredict, which is obvious from the plot.
# Soon after day 10 the model tends to predict O2 around 2 mg/L too low.
# But the shape of the trajectory is correct, suggesting that we
# just have a parameter value problem here.

# Let's save results, first dropping that annoying index column
dat = dat.iloc[:, 1:4]
dat.head()
dat.to_csv("output/val_dat.csv", index = False)

# And export model fit (note that you need to have the list bit)
fit = pd.DataFrame([{"MAE": MAE, "MBE": MBE}])
fit.to_csv("output/val_fit.csv", index = False)
