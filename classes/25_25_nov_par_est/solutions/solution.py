"""
File: solution.py

Author: Sasha D. Hafner

Description:
    Solution to parameter estimation exercise.
"""

# Packages/modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import O2dc_mods as oxm
from scipy.optimize import least_squares

# 1. Graphical validation

# Get measurement data
# Get measurements
O2_meas_dat = pd.read_csv('meas_data/O2.csv')
OM_meas_dat = pd.read_csv('meas_data/OM.csv')

# Inspect
O2_meas_dat
OM_meas_dat

pred01 = oxm.O2dc(
    L= 1,               # m
    dx=0.01,            # m
    k= 1E-4,            # m3/kg-d
    tmax=60 * 86400,    # 60 d
    nt=61,
    O2_init=0.008,       # kg/m3
    OM_init=0.01,         # kg/m3 (20 mg/L) 
    O2_sat= 0.01,         # kg/m3 (10 mg/L)
    D={                   # m2/s 
        "O2": 2E-9,
        "OM": 2E-9
    }
)

# Extract results and do some unit conversion
# Convert to mg/L
# Bottom O2 node
O2_bot = 1000 * pred01["O2"][-1, :]
# Middle OM
OM_mid = 1000 * pred01["OM"][51, :]
# Convert time to days
days = pred01["t"]/60/60/24

# Plot O2 measurements and model
plt.close()
plt.plot(days, O2_bot, label = "Model")
plt.plot(O2_meas_dat.time_d, O2_meas_dat.bottom_O2_mg_L, "ro", label='Measurements')
plt.ylabel("Bottom $\\mathrm{O}_2$ concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend(loc=1)
plt.savefig("plots/O2_conc_val1.png")

# Plot OM and model 
plt.close()
plt.plot(days, OM_mid, label="Model")
plt.plot(OM_meas_dat.time_d, OM_meas_dat.OM_mg_L, "bo", label='Measurements')
plt.ylabel("Middle OM concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend(loc=1)
plt.savefig("plots/OM_conc_val1.png")

# See model predict much too much of a drop in O2 
# But OM predictions not as far off

# 2. Parameter estimation from O2 measurements

# A. New model function with arbitrary times
# Test it
pred02 = oxm.O2dct(
    L= 1,
    dx=0.01,
    k= 1E-4,
    t_eval=O2_meas_dat.time_d * 86400,
    O2_init=0.008,
    OM_init=0.01,
    O2_sat= 0.01,
    D={
        "O2": 2E-9,
        "OM": 2E-9
    }
)

pred02

# B. Residuals function
# O2dc() parameters are hard-coded for now
def res_func_O2(x, O2_meas, times):

    """
    Function for calculating residuals for ...

    Parameters
    ----------
    x : float
        Guess for values 
    ...

    Returns
    -------
    np.ndarray
        Residuals
    """

    # Model call
    pred = oxm.O2dct(
        L= 1,
        dx=0.01,
        k= x[0],
        t_eval=times,
        O2_init=0.008,
        OM_init=0.01,
        O2_sat= 0.01,
        D={
            "O2": x[1],
            "OM": x[1], 
        },
    )

    # Calculate residuals
    res = pred["O2"][-1, :] - O2_meas

    # Return residuals
    return res

# Test it
O2 = O2_meas_dat["bottom_O2_mg_L"] / 1000 
times = O2_meas_dat["time_d"] * 86400

res_func_O2([1E-4, 2E-9], O2, times)

# Compare to plot--looks about right

# C. Put it together with least_squares
#lspar = least_squares(
#    res_func_O2, 
#    x0=[1E-4, 10 * 2E-9], 
#    args=(
#        O2, 
#        times, 
#    )
#)
#
#lspar.x

# Try a better first guess for D
lspar=least_squares(
    res_func_O2, 
    x0=[1E-4, 1E-7], 
    args=(
        O2, 
        times, 
    )
)

lspar.x

# Let's save these estimates in a dictionary for comparison

pars = {
        "2": 0,
        "3": 0,
        "4": 0,
}

pars["2"] = np.round(np.log10(lspar.x), 2)

# Results seem stable

## Try much lower reaction value--that could also explain higher O2
#lspar = least_squares(
#    res_func, 
#    x0=[1E-6, 2E-9], 
#    args=(
#        O2, 
#        times, 
#    )
#)
#
#lspar.x

# Run model and plot results!
pred02 = oxm.O2dc(
    L= 1,               # m
    dx=0.01,            # m
    k= lspar.x[0],      # m3/kg-d
    tmax=60 * 86400,    # 60 d
    nt=61,
    O2_init=0.008,       # kg/m3
    OM_init=0.01,         # kg/m3 (20 mg/L) 
    O2_sat= 0.01,         # kg/m3 (10 mg/L)
    D={                   # m2/s 
        "O2": lspar.x[1],
        "OM": lspar.x[1],
    }
)

# Extract results and do some unit conversion
# Convert to mg/L
# Bottom O2 node
O2_bot = 1000 * pred02["O2"][-1, :]
# Middle OM
OM_mid = 1000 * pred02["OM"][51, :]
# Convert time to days
days = pred02["t"]/60/60/24

# Plot O2 measurements and model
plt.close()
plt.plot(days, O2_bot, label="Model")
plt.plot(O2_meas_dat.time_d, O2_meas_dat.bottom_O2_mg_L, "ro", label='Measurements')
plt.ylabel("Bottom $\\mathrm{O}_2$ concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend(loc=1)
plt.savefig("plots/O2_conc_val2.png")

# Plot OM and model 
plt.close()
plt.plot(days, OM_mid, label="Model")
plt.plot(OM_meas_dat.time_d, OM_meas_dat.OM_mg_L, "bo", label='Measurements')
plt.ylabel("Middle OM concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend(loc=1)
plt.savefig("plots/OM_conc_val2.png")

# 3. Use OM for parameter estimation

# We need a new residuals function
def res_func_OM(x, OM_meas, times):

    """
    Function for calculating residuals for ...

    Parameters
    ----------
    x : float
        Guess for values 
    ...

    Returns
    -------
    np.ndarray
        Residuals
    """

    # Use this print() call to help figure out the problem with some least_squares() calls
    #print(x)

    # Model call
    pred = oxm.O2dct(
        L= 1,
        dx=0.01,
        k= x[0],
        t_eval=times,
        O2_init=0.008,
        OM_init=0.01,
        O2_sat= 0.01,
        D={
            "O2": x[1],
            "OM": x[1], 
        },
    )

    # Calculate residuals
    res = pred["OM"][51, :] - OM_meas

    # Return residuals
    return res

# 
OM = OM_meas_dat["OM_mg_L"] / 1000 
times = OM_meas_dat["time_d"] * 86400

# Next block does not work well--problem is negative parameter guesses
# See below
#lspar = least_squares(
#    res_func_OM, 
#    x0=[1E-4, 1E-7], 
#    args=(
#        OM, 
#        times, 
#    )
#)
#
#lspar.x

# Use print(x) in res_func() to find problem--seems to be negative parameter guesses

# Best solution is to set limits with bounds argument
# Could also 

lspar = least_squares(
    res_func_OM, 
    x0=[1E-4, 1E-7], 
    args=(
        OM, 
        times, 
    ),
    bounds=(
        [1E-8, 1E-9], 
        [1E-2, 1E-4], 
    )
)

lspar.x

pars["3"] = np.round(np.log10(lspar.x), 2)

# Run model and plot results
pred03 = oxm.O2dc(
    L= 1,               # m
    dx=0.01,            # m
    k= lspar.x[0],      # m3/kg-d
    tmax=60 * 86400,    # 60 d
    nt=61,
    O2_init=0.008,       # kg/m3
    OM_init=0.01,         # kg/m3 (20 mg/L) 
    O2_sat= 0.01,         # kg/m3 (10 mg/L)
    D={                   # m2/s 
        "O2": lspar.x[1],
        "OM": lspar.x[1],
    }
)

# Extract results and do some unit conversion
# Convert to mg/L
# Bottom O2 node
O2_bot = 1000 * pred03["O2"][-1, :]
# Middle OM
OM_mid = 1000 * pred03["OM"][51, :]
# Convert time to days
days = pred03["t"]/60/60/24

# Plot O2 measurements and model
plt.close()
plt.plot(days, O2_bot, label="Model")
plt.plot(O2_meas_dat.time_d, O2_meas_dat.bottom_O2_mg_L, "ro", label='Measurements')
plt.ylabel("Bottom $\\mathrm{O}_2$ concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend(loc=1)
plt.savefig("plots/O2_conc_val3.png")

# Plot OM and model 
plt.close()
plt.plot(days, OM_mid, label="Model")
plt.plot(OM_meas_dat.time_d, OM_meas_dat.OM_mg_L, "bo", label='Measurements')
plt.ylabel("Middle OM concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend(loc=1)
plt.savefig("plots/OM_conc_val3.png")


# 4. Combined

# With different variables, it would be tricky to program a completely flexible approach
# Better to hard-code this as below

# We need another residuals function
# There are many ways to organize inputs!
# Perhaps dictionaries or a single one would be more efficient than what we've done below
def res_func_2v(
    x, 
    O2_meas, 
    O2_times, 
    O2_weights, 
    OM_meas, 
    OM_times, 
    OM_weights
):

    """
    Function for calculating residuals for ...

    Parameters
    ----------
    x : float
        Guess for values 
    ...

    Returns
    -------
    np.ndarray
        Residuals
    """

    # Use this print() call to help figure out the problem with some least_squares() calls
    #print(x)

    # We will call the model twice because times could (and do) differ
    # We could do something more clever (and efficient) with slicing 
    # (combine O2_times and OM_times, call model for unique values, 
    # then extract only those times that correspond to the inputs
    # in order to calculate residuals. But we did not do that here!
    # First model call is for OM residuals, so we need to use OM_times.
    pred1 = oxm.O2dct(
        L= 1,
        dx=0.01,
        k= x[0],
        t_eval=OM_times,
        O2_init=0.008,
        OM_init=0.01,
        O2_sat= 0.01,
        D={
            "O2": x[1],
            "OM": x[1], 
        },
    )

    # Calculate residuals
    OM_res = OM_weights * (pred1["OM"][51, :] - OM_meas)

    # And second is for O2, where only t_eval values differ from the
    # call above
    pred2 = oxm.O2dct(
        L= 1,
        dx=0.01,
        k= x[0],
        t_eval=O2_times,
        O2_init=0.008,
        OM_init=0.01,
        O2_sat= 0.01,
        D={
            "O2": x[1],
            "OM": x[1], 
        },
    )

    # Calculate residuals
    O2_res = O2_weights * (pred2["O2"][-1, :] - O2_meas)

    res = np.concatenate([OM_res, O2_res])

    #print(sum(res**2))

    # Return residuals
    return res

# Now for parameter estimation
# First get measurements we need
OM_meas = OM_meas_dat["OM_mg_L"] / 1000 
OM_times = OM_meas_dat["time_d"] * 86400
O2_meas = O2_meas_dat["bottom_O2_mg_L"] / 1000 
O2_times = O2_meas_dat["time_d"] * 86400

# For weights, let's make sure the sum of OM weights = sum of O2 weights
# We can do that based on the number of observations
OM_weights = np.full_like(OM_meas, 1 / len(OM_meas))
O2_weights = np.full_like(O2_meas, 1 / len(O2_meas))

OM_weights
O2_weights

# Check
sum(OM_weights)
sum(O2_weights)
# Perfect

# And run least_squares(), including bounds (no reason to leave them out!)
lspar = least_squares(
    res_func_2v, 
    x0=[1E-4, 1E-7], 
    args=(
        O2_meas,
        O2_times,
        O2_weights,
        OM_meas,
        OM_times,
        OM_weights,
    ),
    bounds=(
        [1E-8, 1E-9], 
        [1E-2, 1E-4], 
    )
)

lspar.x
lspar

pars["4"] = np.round(np.log10(lspar.x), 2)

# Run model and plot results
pred04 = oxm.O2dc(
    L= 1,               # m
    dx=0.01,            # m
    k= lspar.x[0],      # m3/kg-d
    tmax=60 * 86400,    # 60 d
    nt=61,
    O2_init=0.008,      # kg/m3
    OM_init=0.01,       # kg/m3 (20 mg/L) 
    O2_sat= 0.01,       # kg/m3 (10 mg/L)
    D={                 # m2/s 
        "O2": lspar.x[1],
        "OM": lspar.x[1],
    }
)

pred01["O2"]
pred04["O2"]

# Extract results and do some unit conversion
# Convert to mg/L
# Bottom O2 node
O2_bot = 1000 * pred04["O2"][-1, :]
# Middle OM
OM_mid = 1000 * pred04["OM"][51, :]
# Convert time to days
days = pred04["t"]/60/60/24

# Plot O2 measurements and model
plt.close()
plt.plot(days, O2_bot, label="Model")
plt.plot(O2_meas_dat.time_d, O2_meas_dat.bottom_O2_mg_L, "ro", label='Measurements')
plt.ylabel("Bottom $\\mathrm{O}_2$ concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend(loc=1)
plt.savefig("plots/O2_conc_val4.png")

# Plot OM and model 
plt.close()
plt.plot(days, OM_mid, label="Model")
plt.plot(OM_meas_dat.time_d, OM_meas_dat.OM_mg_L, "bo", label='Measurements')
plt.ylabel("Middle OM concentration ($\\mathrm{mg}~\\mathrm{L}^{-1}$)")
plt.xlabel("Time after filling (d)")
plt.legend(loc=1)
plt.savefig("plots/OM_conc_val4.png")

# Try different starting values

lspar = least_squares(
    res_func_2v, 
    x0=[1E-5, 2E-7], 
    args=(
        O2_meas,
        O2_times,
        O2_weights,
        OM_meas,
        OM_times,
        OM_weights,
    ),
    bounds=(
        [1E-8, 1E-9], 
        [1E-2, 1E-4], 
    )
)

lspar.x
lspar

print(pars)
