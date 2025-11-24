
"""
File: par_est4.py

Author: Sasha D. Hafner 

Description:
    Parameter estimation demo using the ice melting model with two 
    sets of measurements.
"""

# Python packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import least_squares
import ice_mods as im

# Measurements
# Mass is in g
# Notice that we are no longer adding new columns with the model units.
# This is an alternative approach.
# Important thing is to be careful and be consistent in units model
# sees.
meas = pd.read_csv("meas_data/ice_meas.csv")
time_meas = meas["time_min"] * 60.
ice_mass_meas_1 = meas.ice_g_1 / 1000
ice_mass_meas_2 = meas.ice_g_2 / 1000
temp_air_meas = np.mean(meas.temp_air)
mass_0_meas_1 = ice_mass_meas_1.iloc[0] 
mass_0_meas_2 = ice_mass_meas_2.iloc[0] 

# There are different approaches we could take, but we'll use a 
# list of dictionaries organize multiple data series

# Residuals function
def res_func(x, meas_sets):

    """
    Function for calculating residuals for ice melting model for parameter estimation.

    Parameters
    ----------
    x : array
        Guess for model parameters for the h parameter (convection heat transfer 
        coefficient) and tlag input in the melt4() model.
    meas_sets : list
        List of dictionaries with measurement data for a different 
        set/series in each element.

    Returns
    -------
    np.ndarray
        Residuals
    """

    res = np.empty(0)

    # Model calls
    for ms in meas_sets:
        pred = im.melt4(
            mass_0 = ms["mass_0"], 
            temp_air = ms["temp_air"], 
            h = x[0],
            tadj = x[1],
            times = ms["time"]
        )
        rr = pred["m"] - ms["ice_mass_meas"]
        res = np.concatenate([res, rr])

    # Return residuals in one line
    return res

meas_sets = [
    {
        "ice_mass_meas": ice_mass_meas_1,
        "mass_0": mass_0_meas_1,
        "temp_air": temp_air_meas,
        "time": time_meas,
    },
    {
        "ice_mass_meas": ice_mass_meas_2,
        "mass_0": mass_0_meas_2,
        "temp_air": temp_air_meas,
        "time": time_meas,
    },
]


# Now do parameter estimation
lspar = least_squares(
    res_func, 
    x0 = [50, 100], 
    args = (meas_sets,)
)

lspar.x
lspar["x"]
lspar.x[0]

# Now we have estimated values for two parameters
# Note a couple things about the code

print(lspar.x)

predval1 = im.melt4(
    mass_0 = mass_0_meas_1, 
    temp_air = temp_air_meas, 
    h = lspar.x[0], 
    tadj = lspar.x[1], 
    times =  time_meas
)

predval2 = im.melt4(
    mass_0 = mass_0_meas_2, 
    temp_air = temp_air_meas, 
    h = lspar.x[0], 
    tadj = lspar.x[1], 
    times =  time_meas
)

# Plot
plt.close()
plt.plot(meas.time_min / 60, meas.ice_g_1, "r.")
plt.plot(predval1["t"] / 3600, 1000 * predval1["m"], "r-")
plt.plot(meas.time_min / 60, meas.ice_g_2, "b.")
plt.plot(predval2["t"] / 3600, 1000 * predval2["m"], "b-")
plt.xlabel("Time (h)")
plt.ylabel("Ice mass (g)")
plt.savefig("plots/sol4.png")

# Do you know why predictions differ for the two ice cubes?
# Not parameter values!
