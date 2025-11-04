
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
dx = 0.01 # meter
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
    
    J_left = -D * (c[1] - c_left)/(2*dx)
    J_right = -D * (c_right - c[-2])/(2*dx)
    
    dQ_left = J_left
    dQ_right = J_right
    
    return np.concatenate((dcdt,np.array([dQ_left, dQ_right])))

c0 = np.zeros(len(x_grid))
c0[0] = 0
c0 = np.concatenate((c0, np.array([0,0])))
c_left = 10
c_right = 0
tmax = 1000 # s

sol = solve_ivp(rates, t_span = [0, tmax], y0 = c0, method = 'LSODA',
                t_eval = np.linspace(0, tmax, 50),
                args = (dx, x_grid, c_left, c_right))
      

J_left = sol.y[-2,:]
J_right = sol.y[-1,:]

plt.plot(sol.t, J_left)
plt.plot(sol.t, J_right)

O2 = sol.y[:len(x_grid),:]
net_flux_in = J_left[-1] - J_right[-1]
total = np.trapz(O2, x_grid, axis = 0)

net_flux_in
total[-1]


def rates2(t, c, dx, x_grid):
    
    dcdt = np.zeros(len(x_grid))
    N = len(x_grid)-1
    
    c = c[:N]
    
    dcdt[0] = 0
    dcdt[-1] = 0
    
    for i in range(1, N-1):
        dcdt[i] = D * (c[i-1] - 2 * c[i] + c[i+1])/dx**2
    
    J_left = -D * (c[1] - c[0])/(dx)
    J_right = -D * (c[-1] - c[-2])/(dx)
    
    dQ_left = J_left
    dQ_right = J_right
    
    return np.concatenate((dcdt,np.array([dQ_left, dQ_right])))

c0 = np.zeros(len(x_grid))
c0[0] = 10
c0 = np.concatenate((c0, np.array([0,0])))
tmax = 1000 # s

sol2 = solve_ivp(rates2, t_span = [0, tmax], y0 = c0, method = 'LSODA',
                t_eval = np.linspace(0, tmax, 50),
                args = (dx, x_grid))

J_left = sol.y[-2,:]
J_right = sol.y[-1,:]

plt.plot(sol.t, J_left)
plt.plot(sol.t, J_right)

O2 = sol.y[:len(x_grid),:]
net_flux_in = J_left[-1] - J_right[-1]
total = np.trapz(O2, x_grid, axis = 0)

net_flux_in - total[-1]
total[-1]
