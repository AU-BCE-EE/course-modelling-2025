"""
File: mass_bal.py
Author: Sasha Hafner and Frederik Dalby
Course: Modelling 2025

Description:
    Mass balance verification of O2 reaction-transport model.
"""

# Load packages and modules
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
import O2dc_mods as oxm

# Review the mass balance equation
"""
Start with:
Rate of O2 accumulation in lagoon = rate of O2 diffusion in - rate of O2 consumption by reaction

But here we will look at some total over a simulation, so:

O2 accumulation in lagoon = cumulative O2 diffusion in - cumulative O2 consumption by reaction

And then for OM:

OM accumulation in lagoon = - cumulative OM consumption by reaction

Or, clearer:

OM depletion in lagoon = cumulative OM consumption by reaction

To check a mass balance we need to separately estimate multiple terms.
For OM we cannot--the model only tracks OM accumulation and nothing else for OM.

But for O2 our model tracks cumulative O2 diffusion into the lagoon, so we can compare that to the change in dissolved O2 to check for a mistake.
"""


# 1. Test O2 mass balance with no respiration and no initial dissolved O2
# dx should not matter here (remember this is verification) but 1E-3 
# is pretty fast still
pred01 = oxm.O2dc(
    L = 0.1,
    dx = 0.001,
    k = 0,              # Set respiration to 0
    tmax = 10 * 86400,
    nt = 100,
    O2_init  =  0,      # Set intial O2 to 0
    OM_init =  0.1,
    O2_sat   = 0.010,
    D = {
        "O2": 2.1E-9,
        "OM": 1.5E-9
    }
)

# Mass transfer of O2 in at the top
x = pred01["x"]
O2_in = pred01["O2_in"]
O2 = pred01["O2"]
O2_in_f = O2_in[-1]
O2_accum = np.trapezoid(O2, x, axis = 0)[-1]

# The sum of O2 in the sys should be equal to the in in-out of sys
# when respiration is off. 

# Verifying this:
# O2 accumulation in lagoon = cumulative O2 diffusion in - cumulative O2 consumption by reaction

# Or really, this, because the reaction rate is zero:
# O2 accumulation in lagoon = cumulative O2 diffusion in

O2_in_f 
O2_accum
O2_in_f - O2_accum

# Try with some O2 at start
# 2. Include respiration and O2 at the start
pred02 = oxm.O2dc(
    L = 0.1,
    dx = 0.001,
    k = 2E-5,  
    tmax = 10 * 86400,
    nt = 100,
    O2_init  =  0.01,
    OM_init =  0.1,
    O2_sat   = 0.010,
    D = {
        "O2": 2.1E-9,
        "OM": 1.5E-9
    }
)


# Mass transfer of O2 in at the top
O2_in = pred02["O2_in"]
O2 = pred02["O2"]
OM = pred02["OM"]
O2_in_f = O2_in[-1]

# For O2 accumulation, we now need to consider O2 present at the start
# Here _f = final and _i is for initial 
O2_f = np.trapezoid(O2, x, axis = 0)[-1]
O2_i = np.trapezoid(O2, x, axis = 0)[0]
O2_accum = O2_f - O2_i

# Verifying this:
# O2 accumulation in lagoon = cumulative O2 diffusion in - cumulative O2 consumption by reaction

# So we have first two terms, and need last one
# We should be able to get cumulative reaction from change in OM
OM_f = np.trapezoid(OM, x, axis = 0)[-1]
OM_i = np.trapezoid(OM, x, axis = 0)[0]
cum_rxn = OM_i - OM_f

# Now check
O2_accum
O2_in_f
cum_rxn

O2_accum - (O2_in_f - cum_rxn)

# Looks good
# Note that "accumulation" is negative
O2_accum

