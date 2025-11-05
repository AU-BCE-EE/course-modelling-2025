
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 12:38:54 2025

@author: au277187
"""
import numpy as np 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# diffusion in an open pipe with 10 mg/m3 at left side and 0 mg/m3 at right side
# we want to keep those ends fixed, that is dirichlet BC in both ends. 
# This can be done in two ways that are slightly different
#    ----------------------------------
# 10 0  0  0  0  0  0  0  0  0  0  0  0  0                                  
#    ----------------------------------
# 
# The governing equation dc/dt = D * d2c/dx2

D = 0.00002 # m^2/s
L = 1 # meter
dx = 0.02 # meter
x_grid = np.arange(0, L+ dx, dx)

# method 1 we fix the derivative at position 0 and N to 0 
# thereby the initial value will never change in the end points
# by doing so we actually have the boundary exactly at the edge of the domain

def rates(t, c, dx, x_grid):
    
    dcdt = np.zeros(len(x_grid))
    N = len(x_grid)-1
    
    dcdt[0] = 0
    dcdt[-1] = 0
    
    for i in range(1, N-1):
        dcdt[i] = D * (c[i-1] - 2 * c[i] + c[i+1])/dx**2
       
    return dcdt

c0 = np.zeros(len(x_grid))
# we need to set the initial condition to what the boundary condition will be
c0[0] = 10 
tmax = 1000 # s

sol = solve_ivp(rates, t_span = [0, tmax], y0 = c0, method = 'LSODA',
                t_eval = np.linspace(0, tmax, 50),
                args = (dx, x_grid))


# Method 2. We chose that the boundary condition is 1 dx left and 1 dx right 
# to the model domain. So the ghost points need to be the boundary values
# we have to pass these values into the rates function as c_left and c_right
def rates2(t, c, dx, x_grid, c_left, c_right):
    
    dcdt = np.zeros(len(x_grid))
    N = len(x_grid)-1

    # instead of fixing dcdt = 0, we use the governing equation and 
    # put c_left at the position before c[0]  
    dcdt[0] = D * (c_left - 2 * c[0] + c[1])/dx**2
    # and after c[-1]
    dcdt[-1] = D * (c[-2] - 2 * c[-1] + c_right)/dx**2
    
    for i in range(1, N-1):
        dcdt[i] = D * (c[i-1] - 2 * c[i] + c[i+1])/dx**2
   
    return dcdt

c0 = np.zeros(len(x_grid))
# using this approach we no longer have to set the initial condition to
# the boundary condition. 
c0[0] = 0
c_left = 10
c_right = 0
tmax = 1000 # s

sol2 = solve_ivp(rates2, t_span = [0, tmax], y0 = c0, method = 'LSODA',
                t_eval = np.linspace(0, tmax, 50),
                args = (dx, x_grid, c_left, c_right))
      
# lets plot the two methods against each other: 
# method 1    
O2 = sol.y[:len(x_grid),:]
# we can calculate the total mass of O2 in the domain at all times by 
# using trapezoidal integration function np.trapz()
total = np.trapz(O2, x_grid, axis = 0)
# the last value in that integration is the total amount of O2 at the last time point
last_total = total[-1]

# we do the same for method 2
O2_2 = sol2.y[:len(x_grid),:]
total_2 = np.trapz(O2_2, x_grid, axis = 0)
last_total_2 = total_2[-1]

# lets plot O2 from the two methods. 
plt.plot(x_grid, O2[:,-1], label = 'method 1: dcdt[0] = 0')
plt.plot(x_grid, O2_2[:,-1], label = 'method 2: dcdt[0] = D*(c_left-2c[0]+c[1])/dx**2')
plt.xlabel('x, meter')
plt.ylabel('conc, mg/m3')
plt.legend(loc = 1)

# lets now compare the total O2 in the system at last time point
print(last_total)
print(last_total_2)

# so first method gives most O2. That makes sense, because the c[0] always 
# contains the saturated O2 value, whereas in method 2 c[0] starts at 0 and 
# has to wait for O2 to diffuse into it from c_left. 



