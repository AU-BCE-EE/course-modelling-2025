
"""
File: par_est2.py

Author: Sasha D. Hafner 

Description:
    Better parameter estimation demo using the ice melting model.
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
meas["ice_kg_1"] = meas["ice_g_1"] / 1000.
ice_mass_meas = meas.ice_kg_1
temp_air_meas = np.mean(meas.temp_air)
mass_0_meas = ice_mass_meas.iloc[0] 

# Residuals function
def res_func(x, ice_mass_meas, mass_0, temp_air, time):

    """
    Function for calculating residuals for ice melting model for parameter estimation.

    Parameters
    ----------
    x : float
        Guess for values for the h parameter (convection heat transfer 
        coefficient) in the melt2() model.
    ice_mass_meas : array
        Measurements of ice mass over time given in times argument (kg)
    mass_0 : float
        Initial ice mass for model input (kg)
    temp_air : float
        Air temperature (deg. C)
    times : array
        Times of mass measurements (s)

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
    res =  pred["m"] - ice_mass_meas

    # Return residuals
    return res

# Now do parameter estimation
lspar = least_squares(
    res_func, 
    x0 = 50, 
    args = (
        ice_mass_meas, 
        mass_0_meas, 
        temp_air_meas, 
        time_meas
    )
)

# Check results
lspar.x
lspar["x"]
lspar.x[0]

# We should get the same estimate as before
