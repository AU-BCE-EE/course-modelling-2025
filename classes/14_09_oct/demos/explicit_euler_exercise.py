# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 16:42:21 2025

@author: au277187
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# this is explicit euler method on a 1D diffusion problem 
# in a pipe

D = 1 
x_start = 0 
x_end = 1 
nx = 100 
dx = (x_end - x_start)/nx 
t_start = 0 
t_end = 1 
nt = 100 
dt = (t_end - t_start)/nt
x = np.arange(x_start, x_end + dx, dx) 

y = np.zeros((nt + 1, nx + 1)) 
A = (0.02/2)**2 * np.pi 
y[0, 0] = 10/(A*dx) 

for i in range(0, nt):
     
    y[i + 1, 0] = y[i, 0] + dt * D * (y[i, 1] - 2*y[i, 0] + y[i, 1])/dx**2
    y[i + 1, nx] = y[i, nx] + dt * D * (y[i, nx-1] - 2*y[i, nx] + y[i, nx-1])/dx**2
    
    for j in range(1, nx):
        y[i + 1, j] = y[i, j] + dt * D * (y[i, j-1] - 2*y[i, j] + y[i, j+1])/dx**2
  
t_grid = np.linspace(t_start, t_end, nt + 1)

for i in range(0, len(x), 2):
   plt.plot(t_grid, y[:,i])

plt.show()
