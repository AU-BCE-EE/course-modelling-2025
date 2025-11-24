"""
File: par_est1.py

Author: Sasha D. Hafner 

Description:
    Basic parameter estimation demo using the melting ice model.
"""

# Python packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Let's keep this handy in case we need to change the model functions
#from importlib import reload

# We need to get least_squares() from the scipy.optimize module
# Normal approach is to get only that function when we just need one 
from scipy.optimize import least_squares

# Our module
import ice_mods as im

# Keep this handy
#reload(im)

# Let's take practical parameter estimation in steps

# 1. Get measurements and convert to units used by the model
# Mass is in g
meas = pd.read_csv("meas_data/ice_meas.csv")
meas["time_sec"] = meas["time_min"] * 60.
meas["ice_kg_1"] = meas["ice_g_1"] / 1000.

# 2. Extract time, temperature, and ice mass to make following steps 
# simpler
time_meas = meas.time_sec
ice_mass_meas = meas.ice_kg_1
temp_air_meas = np.mean(meas.temp_air)
mass_0_meas = ice_mass_meas.iloc[0] 

# 3. Check model call to make sure we know how to call function
# correctly.
# We will use the melt2() model (note the `2`).
pred = im.melt2(
    mass_0 = mass_0_meas, 
    temp_air = temp_air_meas, 
    h = 50, 
    times =  time_meas
)

# Does output look right?
pred

# Plot it

plt.close()
plt.plot(time_meas, ice_mass_meas, "ro")
plt.plot(time_meas, pred["m"], "b-")
plt.savefig("plots/comp1.png")

# 4. Create residuals function
# Create a function that will return residuals, which will be used by 
# least_squares() to calculate the value of the cost function

# Simplest approach is to use only a single function parameter and 
# pass others through the global namespace--we will do that here but 
# use a better approach in following scripts
def res_func(x):

    """
    Function for calculating residuals for ice melting model for 
    parameter estimation. This version uses objects in the global 
    namespace.

    Parameters
    ----------
    x : float
        Guess for values for the h parameter (convection heat transfer 
        coefficient) in the melt2() model.

    Returns
    -------
    np.ndarray
        Residuals
    """

    # Model call
    pred = im.melt2(
        mass_0=mass_0_meas, 
        temp_air=temp_air_meas, 
        h=x,                      # The parameter guess x!
        times=time_meas
    )

    # Calculate residuals 
    res = pred["m"] - ice_mass_meas

    # Return residuals
    return res

# Test it
res_func(50)

# Does that match the plot?

# 5. Parameter estimation with least_squares()
# Now put it together
# All we need is the name of the function and an initial guess

# The least_squares() function calls res_func() with different values
# of h until it settles on the best value

lspar = least_squares(res_func, x0 = 50)
lspar
lspar.x
lspar["x"]
lspar.x[0]

lspar = least_squares(res_func, x0 = 150)
lspar.x

# So our best-fit estimate is 88.4 W/m2-K

# We should, in the very least, do some graphical validation with this value
predval = im.melt2(
    mass_0 = mass_0_meas, 
    temp_air = temp_air_meas, 
    h = lspar.x[0], 
    times =  time_meas
)

plt.close()
plt.plot(meas.time_sec / 3600, 1000 * meas.ice_kg_1, "k.")
plt.plot(predval["t"] / 3600, 1000 * predval["m"])
plt.xlabel("Time (h)")
plt.ylabel("Ice mass (g)")
plt.savefig("plots/sol1.png")



