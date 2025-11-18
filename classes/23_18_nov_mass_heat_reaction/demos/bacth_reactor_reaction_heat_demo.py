# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 15:19:22 2025

@author: au277187
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

T0 = 323
cA0 = 500 # kg/m3
Hrxn = 25700 # J/mole
molar_mass = 80.04 # g/mole
H_rxn = Hrxn / (molar_mass/1000) #
V = 1 # m3
rho = 1000 # kg/m3
Cp = 4180 # J/(kg*K)
A = 1000 # 1/s
Ea = 3 * 10**4 # J/mole
R = 8.314 # J/(mole K)
# initial conditions
y0 = [cA0 * V, T0]

def rates(t, y, V, rho, Cp, H_rxn, A, Ea, R):
    
    mA = y[0]
    T = y[1]
    
    cA = mA/V
    
    k = A * np.exp(-Ea/(R*T))
    r = -k * cA # kg/(s*m3)
    dmAdt = r * V
    
    qrxn = H_rxn * r * V
    
    m = rho * V
    
    dTdt = qrxn /(Cp * m)
    
    return np.array([dmAdt, dTdt])
    
tmax = 1000

sol = solve_ivp(rates, t_span = [0, tmax], y0 = y0,
                t_eval = np.linspace(0, tmax, 100),
                args = (V, rho, Cp, H_rxn, A, Ea, R))


plt.plot(sol.t, sol.y[0])
plt.xlabel('Time, s')
plt.ylabel('kg')

plt.plot(sol.t, sol.y[1])
plt.xlabel('Time, s')
plt.ylabel('temp, K')

