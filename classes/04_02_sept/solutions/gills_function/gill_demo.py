"""
File: gills.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    Some calculations on oxygen transfer flux through fish gills, based
    on a simple mass transfer coefficient approach implemented as a
    function named gill_flux().
"""

# Import packages that will be used in this script
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

# Import the gill_mod module, defined by a script in the working directory
import gill_mod as gm
# Reload as needed during function development
#reload(gm)

# Generate a list of kc values (m/s)
kc = [1.e-4, 4.e-5] 

# Now calculate the oxygen mass flux for all these conditions using the function
# We can check the arguments by looking at the script gill_mod.py or with help()
help(gm.gill_flux)
flux = gm.gill_flux(kc, cw = 10)
print(flux)

# The function could make calculations for a larger array of kc values
dkc = 0.1
kc = 10**np.arange(-6, -3 + dkc, dkc) 
flux = gm.gill_flux(kc, cw = 10)

# Let's plot them
plt.close()
plt.plot(kc, flux)
plt.savefig('oxygen_flux.png')
