
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 12:38:54 2025

@author: au277187
"""
import numpy as np 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# diffusion in an open pipe with 10 mg/m3 at very left side to start with
#  ----------------------------------
# 0  0  0  0  0  0  0  0  0  0  0  0                                  
#  ----------------------------------
# 
# dc/dt = D * d2c/dx2

D = 0.00002 # m^2/s
L = 1 # meter
dx = 0.001 # meter
x_grid = np.arange(0, L+ dx, dx)
tmax = 1000 # max time, s

def rates(t, c, dx, x_grid, c_left, c_right):
    
    dcdt = np.zeros(len(x_grid))
    N = len(x_grid)-1
    
    c = c[:N]
    
    dcdt[0] = D * (c_left - 2 * c[0] + c[1])/dx**2
    dcdt[-1] = D * (c[-2] - 2 * c[-1] + c_right)/dx**2
    
    for i in range(1, N-1):
        dcdt[i] = D * (c[i-1] - 2 * c[i] + c[i+1])/dx**2
   
    return dcdt

c0 = np.zeros(len(x_grid))
c0[0] = 0
c_left = 10
c_right = 0
tmax = 1000 # s

sol = solve_ivp(rates, t_span = [0, tmax], y0 = c0, method = 'LSODA',
                t_eval = np.linspace(0, tmax, 50),
                args = (dx, x_grid, c_left, c_right))
      
def rates2(t, c, dx, x_grid):
    
    dcdt = np.zeros(len(x_grid))
    N = len(x_grid)-1
    
    c = c[:N]
    
    dcdt[0] = 0
    dcdt[-1] = 0
    
    for i in range(1, N-1):
        dcdt[i] = D * (c[i-1] - 2 * c[i] + c[i+1])/dx**2
       
    return dcdt

c0 = np.zeros(len(x_grid))
c0[0] = 10
tmax = 1000 # s

sol2 = solve_ivp(rates2, t_span = [0, tmax], y0 = c0, method = 'LSODA',
                t_eval = np.linspace(0, tmax, 50),
                args = (dx, x_grid))

O2_1 = sol.y[:len(x_grid),:]
total_1 = np.trapz(O2_1, x_grid, axis = 0)
total_1[-1]

O2_2 = sol2.y[:len(x_grid),:]
total_2 = np.trapz(O2_2, x_grid, axis = 0)
total_2[-1]

plt.plot(x_grid, O2_1[:,-1])
plt.plot(x_grid, O2_2[:,-1])
