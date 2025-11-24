
"""
File: par_est2.py

Author: Sasha D. Hafner 

Description:
    Parameter estimation demo using the ice melting model.
    This version uses weights with single parameter optimization.
    It is not a particularly convincing result!
"""

# Python packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import least_squares
import ice_mods as im

# Measurements
# Mass is in g
meas = pd.read_csv("meas_data/ice_meas.csv")
time_meas = meas["time_min"] * 60.
ice_mass_meas = meas.ice_g_1 / 1000.
temp_air_meas = np.mean(meas.temp_air)
mass_0_meas = ice_mass_meas.iloc[0] 

# Residuals function
def res_func(x, ice_mass_meas, mass_0, temp_air, time, weights):

    """
    Function for calculating residuals for ice melting model for parameter estimation.

    Parameters
    ----------
    x : float
        Guess for values for the h parameter (convection heat transfer 
        coefficient) in the melt2() model.
    mass_0 : float
        Initial ice mass for model input (kg)
    temp_air : float
        Air temperature (deg. C)
    times : array
        Times of mass measurements (s)
    weights : array
        Weights for weighting residuals
    Returns
    -------
    np.ndarray
        Residuals
    """

    # Model call
    pred = im.melt2(
        mass_0 = mass_0, 
        temp_air = temp_air, 
        h = x,                     # This is where the parameter guess x goes for this model
        times = time
    )

    # Calculate residuals
    res =  weights * (pred["m"] - ice_mass_meas)

    # Return residuals
    return res


# Now do parameter estimation

# Create weights array
weights = np.full_like(ice_mass_meas, 1.)
# Say we don't trust the last 4 values at all
weights[-4:] = 0.

lspar = least_squares(
    res_func, 
    x0 = 50, 
    args = (
        ice_mass_meas, 
        mass_0_meas, 
        temp_air_meas, 
        time_meas,
        weights
    )
)

lspar.x
lspar["x"]
lspar.x[0]
print(lspar.x)

predval = im.melt2(
    mass_0 = mass_0_meas, 
    temp_air = temp_air_meas, 
    h = lspar.x[0], 
    times =  time_meas
)

# Plot
plt.close()
plt.plot(meas.time_min / 60, meas.ice_g_1, "k.")
plt.plot(predval["t"] / 3600, 1000 * predval["m"])
plt.xlabel("Time (h)")
plt.ylabel("Ice mass (g)")
plt.savefig("plots/sol5.png")
