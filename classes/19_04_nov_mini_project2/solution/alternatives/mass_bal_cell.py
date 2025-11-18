"""
File: mass_bal.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    Mass balance check of cell-based O2 diffusion model
"""

import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

import O2dc_cell_mods as oxm

reload(oxm)

# Case 1 with all processes: OK
pred01 = oxm.O2dcc(
    L = 0.05,
    N = 5,
    k = 1E-6,
    tmax = 86400.,
    nt =       5,
    S_init  =  1.,
    O2_init =  0.01,
    O2_sat   = 0.01,
    D = {
        "O2": 2.1E-9,
        "S": 1.5E-9
    }
)

# Check mass balance
# O2 accum = O2 in - O2 consumed

O2f = sum(pred01["O2"][:, -1] * pred01["dx"])
O2i = sum(pred01["O2"][:, 0] * pred01["dx"])
Sf = sum(pred01["S"][:, -1] * pred01["dx"])
Si = sum(pred01["S"][:, 0] * pred01["dx"])
(O2f - O2i) - (pred01["O2in"][-1] - (Si - Sf))

# Case 2 with no respiration: OK
pred01 = oxm.O2dcc(
    L = 0.05,
    N = 10,
    k = 0.,
    tmax = 86400.,
    nt =       5,
    S_init  =  1.,
    O2_init =  0.01,
    O2_sat   = 0.01,
    D = {
        "O2": 2.1E-9,
        "S": 1.5E-9
    }
)

O2f = sum(pred01["O2"][:, -1] * pred01["dx"])
O2i = sum(pred01["O2"][:, 0] * pred01["dx"])
Sf = sum(pred01["S"][:, -1] * pred01["dx"])
Si = sum(pred01["S"][:, 0] * pred01["dx"])
(O2f - O2i) - (pred01["O2in"][-1] - (Si - Sf))

# Case 3 with no respiration and initial O2 of zero: OK
pred01 = oxm.O2dcc(
    L = 0.05,
    N = 10,
    k = 0.,
    tmax = 86400.,
    nt =       5,
    S_init  =  1.,
    O2_init =  0.,
    O2_sat   = 0.01,
    D = {
        "O2": 2.1E-9,
        "S": 1.5E-9
    }
)

O2f = sum(pred01["O2"][:, -1] * pred01["dx"])
O2i = sum(pred01["O2"][:, 0] * pred01["dx"])
Sf = sum(pred01["S"][:, -1] * pred01["dx"])
Si = sum(pred01["S"][:, 0] * pred01["dx"])
(O2f - O2i) - (pred01["O2in"][-1] - (Si - Sf))

# Case 4 back to having respiration and initial O2 at sat (like 1) but finer grid: OK
pred01 = oxm.O2dcc(
    L = 0.05,
    N = 100,
    k = 1E-3,
    tmax = 86400.,
    nt =       5,
    S_init  =  1.,
    O2_init =  0.01,
    O2_sat   = 0.01,
    D = {
        "O2": 2.1E-9,
        "S": 1.5E-9
    }
)

O2f = sum(pred01["O2"][:, -1] * pred01["dx"])
O2i = sum(pred01["O2"][:, 0] * pred01["dx"])
Sf = sum(pred01["S"][:, -1] * pred01["dx"])
Si = sum(pred01["S"][:, 0] * pred01["dx"])
(O2f - O2i) - (pred01["O2in"][-1] - (Si - Sf))

# Case 5 with all processes except diffusion: OK
reload(oxm)
pred01 = oxm.O2dcc(
    L = 0.05,
    N = 10,
    k = 1E-3,
    tmax = 86400.,
    nt =       5,
    S_init  =  1.,
    O2_init =  0.01,
    O2_sat   = 0.01,
    D = {
        "O2": 0.,
        "S":  0. 
    }
)

O2f = sum(pred01["O2"][:, -1] * pred01["dx"])
O2i = sum(pred01["O2"][:, 0] * pred01["dx"])
Sf = sum(pred01["S"][:, -1] * pred01["dx"])
Si = sum(pred01["S"][:, 0] * pred01["dx"])
(O2f - O2i) - (pred01["O2in"][-1] - (Si - Sf))

# So cell-based has perfect mass balance ;)




