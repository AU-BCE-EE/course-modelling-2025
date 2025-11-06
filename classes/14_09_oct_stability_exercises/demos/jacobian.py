# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 13:15:40 2025

@author: au277187
"""
import numpy as np
import numdifftools as nd

def dydt(y):
    dydt0 = 1 * y[0] + y[1]
    dydt1 = 0.5 * y[1] - 0.1 * y[0]
    return np.array([dydt0, dydt1])

J_func = nd.Jacobian(dydt)

# test at equilibrium point which is [0,0] from
J_crit = J_func([0, 0])
print(J_crit)

# eigenvalues
print(np.linalg.eigvals(J_crit))

# all real numbers are positiv --> then the system is unstable

def dydt(t,y):
    dydt0 = 1 * y[0] + y[1]
    dydt1 = 0.5 * y[1] - 0.1 * y[0]
    return np.array([dydt0, dydt1])

from scipy.integrate import solve_ivp
sol = solve_ivp(dydt, t_span = [0, 110], y0 = [1,1])

import matplotlib.pyplot as plt

plt.plot(sol.t, sol.y[0])
plt.plot(sol.t, sol.y[1])
