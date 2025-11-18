# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 12:50:48 2025

@author: au277187
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
# bacth reactor with first order reaction 
T0 = 323 # K
cA0 = 500 # kg/m3
A = 1000 # 1/s
Ea = 3 * 10**4 # J/mol
R = 8.314 # J/(mol K)
molar_mass = 80.043 # g/mol
delta_H = 25700 / (molar_mass/1000) # J/kg # endothermic NH4NO3 -> NH4 + NO3
V = 1 # m3
rho = 1000 # kg/m3
Cp = 4180 # J/(kg K)

y0 = [cA0 * V, T0]

def rates(t, y, A, Ea, R, V, rho, Cp, delta_H):
    
    mA = y[0]
    T = y[1]
    
    cA = mA/V
    
    k = A * np.exp(-Ea/(R*T))
    r = -k * cA
    
    # derivative mass
    dmAdt = r * V
    qrxn = delta_H * r * V
    
    m = rho * V    
    dTdt = qrxn /(Cp * m)
    
    return np.array([dmAdt, dTdt])

tmax = 1000

sol = solve_ivp(rates, t_span = [0, tmax], y0 = y0, 
                t_eval = np.linspace(0, tmax, 100),
                args = (A, Ea, R, V, rho, Cp, delta_H))


plt.plot(sol.t, sol.y[0])
plt.xlabel('Time, s')
plt.ylabel('Mass, kg')

plt.plot(sol.t, sol.y[1])
plt.xlabel('Time, s')
plt.ylabel('Temp, K')
