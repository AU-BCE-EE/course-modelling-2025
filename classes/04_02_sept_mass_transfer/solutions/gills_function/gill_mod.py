"""
File: gill_mod.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    Contains a single function for calculating oxygen flux across 
    fish gills based on a mass transfer coefficient approach.
"""

import numpy as np

def gill_flux(kc, cw, cb = 0):
    """
    A simple mass transfer function for oxygen transport through gills.
    """

    # Make sure all inputs are arrays
    kc = np.array(kc)
    cw = np.array(cw)
    cb = np.array(cb)
    
    # Get the concentration difference (g/m3 = mg/L)
    dc = cw - cb
    
    # Now calculate the oxygen mass flux (g/m2-s)
    j = kc * dc
    
    # And return it
    return(j)
