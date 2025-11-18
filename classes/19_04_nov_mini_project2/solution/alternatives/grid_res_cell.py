"""
Checking grid size effect
"""

import numpy as np
import matplotlib.pyplot as plt
from importlib import reload

import O2dc_cell_mods as oxm

reload(oxm)

pred01 = oxm.O2dcc(
    L = 0.1,
    N = 50,
    k = 1E-3,
    tmax = 10 * 86400,
    nt = 20,
    S_init = 1. 
)

pred02 = oxm.O2dcc(
    L = 0.1,
    N = 100,
    k = 1E-3,
    tmax = 10 * 86400,
    nt = 20,
    S_init = 1. 
)

pred03 = oxm.O2dcc(
    L = 0.1,
    N = 200,
    k = 1E-3,
    tmax = 10 * 86400,
    nt = 20,
    S_init = 1. 
)

pred04 = oxm.O2dcc(
    L = 0.1,
    N = 400,
    k = 1E-3,
    tmax = 10 * 86400,
    nt = 20,
    S_init = 1. 
)

pred05 = oxm.O2dcc(
    L = 0.1,
    N = 800,
    k = 1E-3,
    tmax = 10 * 86400,
    nt = 20,
    S_init = 1. 
)



# Check total S as response
sum(pred01["S"] * pred01['dx'])
sum(pred02["S"] * pred02['dx'])
sum(pred03["S"] * pred03['dx'])
sum(pred04["S"] * pred04['dx'])
sum(pred05["S"] * pred05['dx'])

