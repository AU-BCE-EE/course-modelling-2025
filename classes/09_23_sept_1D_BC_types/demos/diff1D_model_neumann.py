
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 12:38:54 2025

@author: au277187
"""
import numpy as np 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# diffusion in an open pipe with 10 mg/m3 in left side to start with
# |-----------------------------------|
# |10  0  0  0  0  0  0  0  0  0  0  0|                                  
# |-----------------------------------|

# 
# dc/dt = D * d2c/dx2

D = 0.00002 # m^2/s
L = 1 # meter
dx = 0.01 # meter
x_grid = np.arange(0, L+ dx, dx)
tmax = 10000 # max time, s

def rates(t, c, dx, x_grid):
    
    dcdt = np.zeros(len(x_grid))
    N = len(x_grid)-1
 
    # J = -D*dc/dx = 0: -D * (c[i+1] - c[i-1])/(2*dx) = 0
    # -D * (c[0+1] - c[0-1])/(2*dx) = 0: c[0-1] is a ghost point
    # -D * (c[0+1] - c[0-1])/(2*dx) = 0: c[0-1] = c[0+1]
    
    dcdt[0] = D * (c[1] - 2 * c[0] + c[1])/dx**2
    # J = -D*dc/dx = 0: -D * (c[i+1] - c[i-1])/(2*dx) = 0
    # At boundary:
    # -D * (c[N+1] - c[N-1])/(2*dx) = 0: c[N+1] is the ghost point
    # c[N+1] = c[N-1]
    
    dcdt[N] = D * (c[N-1] - 2 * c[N] + c[N-1])/dx**2
    
    
    for i in range(1, N):
        dcdt[i] = D * (c[i-1] - 2 * c[i] + c[i+1])/dx**2
    
    return dcdt

c0 = np.zeros(len(x_grid))

c0[0] = 10

tmax = 10000 # s
sol = solve_ivp(rates, t_span = [0, tmax], y0 = c0, method = 'LSODA',
                t_eval = np.linspace(0, tmax, 50),
                args = (dx, x_grid))
      
for i in range(0, len(x_grid)-1, int((len(x_grid)-1)/5)):
    plt.plot(sol.t, sol.y[i], label = i)
plt.legend(loc = 1)
plt.ylabel('concentration, mg/m3')
plt.xlabel('time, s')

