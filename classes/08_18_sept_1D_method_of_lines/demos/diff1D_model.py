
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 12:38:54 2025

@author: au277187
"""
import numpy as np 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# diffusion in an open pipe with 10 mg/m3 in left side to start with
#  ----------------------------------
# 10  0  0  0  0  0  0  0  0  0  0  0                                  
#  ----------------------------------
# 
# dc/dt = D * d2c/dx2

D = 0.00002 # m^2/s
L = 1 # meter
dx = 0.01 # meter
x_grid = np.arange(0, L+ dx, dx)
tmax = 1000 # max time, s

def rates(t, c, dx, x_grid):
    
    dcdt = np.zeros(len(x_grid))
    N = len(x_grid)-1
    
    for i in range(1, N):
        dcdt[i] = D * (c[i-1] - 2 * c[i] + c[i+1])/dx**2
    
    return dcdt

c0 = np.zeros(len(x_grid))
c0[0] = 10

tmax = 1000 # s
sol = solve_ivp(rates, t_span = [0, tmax], y0 = c0, method = 'LSODA',
                t_eval = np.linspace(0, tmax, 50),
                args = (dx, x_grid))
      
for i in range(0, len(x_grid)-1, int((len(x_grid)-1)/5)):
    plt.plot(sol.t, sol.y[i], label = i)
plt.legend(loc = 1)
plt.ylabel('concentration, mg/m3')
plt.xlabel('time, s')

