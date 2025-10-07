# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 13:08:10 2025

@author: au277187
"""
import numpy as np
from scipy.optimize import fsolve

def dydt(y):
    dydt0 = 1 * y[0] + y[1]
    dydt1 = 0.5 * y[1] - 0.1 * y[0]
    return np.array([dydt0, dydt1])

# find the equilibrium points. Look in two different places. 
init_guess = [-100,-100] 
eq = fsolve(dydt, init_guess)
print(eq)

init_guess = [100,100] 
eq = fsolve(dydt, init_guess)
print(eq)
