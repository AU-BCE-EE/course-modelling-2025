"""
Demo of O2 diffusion model
"""

import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

import O2dc_mods_up as oxm

# make some plots of the profiles
reload(oxm)
pred01 = oxm.O2dc_b(
    L = 0.1,                # m
    dx = 0.001,             # m
    k = 0,               # m3/kg-d
    tmax = 2 * 365 * 86400, # 100 d
    nt = 100,
    O2_init = 0.01,         # completely aerobic to start with
    S_init = 0.1,           # kg/m3 (100 mg/L) 
    O2_sat = 0.1,          # kg/m3 (10 mg/L)
    D = {                   # m2/s 
        "O2": 2.1E-9,
        "S": 1.5E-9
    }
)

O2 = pred01["O2"]
S = pred01["S"]
x = pred01["x"]
days = pred01["t"]/60/60/24
dx = pred01["dx"]

# Plot O2 vs. time
plt.close()
plt.plot(days, O2[0, :], label = f'{x[0]} m')
plt.plot(days, O2[round(len(x)/2), :], label = f'{x[round(len(x)/2)]} m')
plt.plot(days, O2[-1, :], label = f'{x[-1]} m')
plt.ylabel('conc (kg/m3)')
plt.xlabel('time, days')
plt.legend(loc = 1)
plt.savefig('plots/O2_conc.png')

# Plot S vs. time
plt.close()
plt.plot(days, S[0, :], label = f'{x[0]} m')
plt.plot(days, S[round(len(x)/2), :], label = f'{x[round(len(x)/2)]} m')
plt.plot(days, S[-1, :], label = f'{x[-1]} m')
plt.ylabel('conc (kg/m3)')
plt.xlabel('time, days')
plt.legend(loc = 1)
plt.savefig('plots/S_conc.png')

# Plot O2 vs. position (profiles)
plt.close()
plt.plot(pred01['O2'][:, 0], pred01['x'])
plt.plot(pred01['O2'][:, 10], pred01['x'])
plt.plot(pred01['O2'][:, 50], pred01['x'])
plt.plot(pred01['O2'][:, 60], pred01['x'])
plt.plot(pred01['O2'][:, 90], pred01['x'])
plt.ylabel('Position (m)')
plt.xlabel('Concentration (kg/m3)')
plt.savefig('plots/O2_profs.png')

plt.close()
plt.plot(pred01['S'][:, 0], pred01['x'])
plt.plot(pred01['S'][:, 10], pred01['x'])
plt.plot(pred01['S'][:, 50], pred01['x'])
plt.plot(pred01['S'][:, 90], pred01['x'])
plt.ylabel('Position (m)')
plt.xlabel('Concentration (kg/m3)')
plt.savefig('plots/S_profs.png')

# verify that mass balance is ok
reload(oxm)
pred02 = oxm.O2dc(
    L = 0.1,
    dx = 0.001,
    k = 0, # set resp to 0
    tmax = 10 * 86400,
    nt = 100,
    O2_init  =  0, # set O2 to 0?
    S_init =  0.1,
    O2_sat   = 0.010,
    D = {
        "O2": 2.1E-9,
        "S": 1.5E-9
    }
)

# fluxes in and out of top and bottom (bottom is 0)
O2_flux_in = pred02['O2_flux_in']
O2_flux_out = pred02['O2_flux_out']
O2 = pred02['O2']
x = pred02["x"]
days = pred02["t"]/60/60/24
dx = pred02["dx"]
net_O2_flux = O2_flux_in[-1] - O2_flux_out[-1]
O2_in_system = np.trapz(O2, x, axis = 0)[-1]

# The sum of O2 in the system should be equal to the flux in-out of system
# when respiration is off. 
net_O2_flux - O2_in_system

pred03 = oxm.O2dc(
    L = 0.1,
    dx = 0.001,
    k = 2E-5, 
    tmax = 60 * 86400, # 60 days
    nt = 30, # 3o output points
    O2_init  =  0.010, # set O2 to saturation point (aearated)
    S_init =  0.1,
    O2_sat   = 0.010,
    D = {
        "O2": 2.1E-9,
        "S": 1.5E-9
    }
)

O2 = pred03["O2"]
x = pred03["x"]
days = pred03["t"]/60/60/24
dx = pred03["dx"]

import pandas as pd
data = pd.read_csv('data/meas_O2.csv')

plt.plot(days, O2[-1,:], label = "model")
plt.plot(data.day, data.bottom_O2_mg_L /1000)

obs = O2[-1,:]
pred = data.bottom_O2_mg_L /1000
MAE = np.sum(np.abs(obs - pred))


# how long it takes to degrade 
pred04 = oxm.O2dc(
    L = 1,
    dx = 0.001,
    k = 2E-5, 
    tmax = 365 * 86400, # 365 days
    nt = 30,            # 30 output points
    O2_init  =  0.010,  # set O2 to saturation point (aerated)
    S_init =  0.1,
    O2_sat   = 0.010,
    D = {
        "O2": 2.1E-9,
        "S": 1.5E-9
    }
)

S = pred04["S"]
x = pred04["x"]
days = pred04["t"]/60/60/24
dx = pred04["dx"]

bottom_S = S[-1,:]
plt.plot(days, bottom_S)
