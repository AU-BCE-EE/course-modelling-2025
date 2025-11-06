# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 08:53:18 2025

@author: au277187
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

D = 2.2*0.00001 # m^2/s
Z = 5 # tank is 5 m tall
R = 2.5 # tank radius is 2.5 meter
dz = 0.25 # step size in z direction
dr = 0.1 # step size in r direction
z_grid = np.arange(0, Z + dz, dz)  # tank is 5 meter high
r_grid = np.arange(0, R + dr, dr) 
ks = 0.0005 # reaction rate constant at wall surface, m/s
ka = 0.00001 # mass transfer at top, m/s
Nr = len(r_grid) # nodes (descritization points) in the r direction
Nz = len(z_grid) # nodes (descritization points) in the z direction
c = np.zeros((Nz, Nr))
c[0,:] = 1000
# solve_ivp() takes a flat (1D array as inital values)
c0_flat = c.flatten(order='F')

def dcdt(t, c_flat, D, dz, dr, ks, ka, Nr, Nz, r_grid):
    
    # Reshape to two dimensions for better intuitive understanding
    c = c_flat.reshape((Nz, Nr), order='F')
    dcdt = np.zeros_like(c)
    
    Ni = Nz - 1 # last index position on z axis
    Nj = Nr - 1 # last index position on r axis
    
    # 1. BC at bottom: 
    # Dirichlet condition where all c(z=0, r) = 1000 ppm.
    # Setting change over time to 0
    # initial conditions
    dcdt[0,:] = 0 # first row (z = 0) and all r (r = :)

    # 2. BC at top: 
    # Robin condition, H2S removal by convection to bulk air 
    # Ficks first law: J = -D * (dC/dz)
    
    # Mass transfer coefficient: J = ka*(C-Cair), C_air = 0
    # ka * (C[Ni,:]) = -D * dC/dz
    # ka * (C[Ni,:]) = -D * (c[Ni+1, :] - c[Ni-1, :])/(2*dz) 
    # isolate the ghost point C[Ni+1,:]. 
    # C_up = c[Ni-1, :] - ka*2*dz*c[Ni, :]/D
    for j in range(1, Nj):
        
        # ghost point above top
        C_up = c[Ni-1, j] - ka*2*dz*c[Ni, j]/D
        
        # diffusion in z dimension at boundary, substitute C_up
        d2cdz2 = (c[Ni-1, j] - 2*c[Ni, j] + C_up) / dz**2
        
        # diffusion in r dimension (nothing special)
        d2cdr2 = (c[Ni, j-1] - 2*c[Ni, j] + c[Ni, j+1]) / dr**2
        dcdr   = (c[Ni, j+1] - c[Ni, j-1]) / (2*dr)
        
        # full governing equation at top boundary
        dcdt[Ni,j] = D * (d2cdz2 + d2cdr2 + 1/r_grid[j] * dcdr)
    
    # 3. BC at left (center)
    # Neumann condition, where we have symmetry in center
    # if symnmetry, then at the center dC/dr = 0.
    # We skip first and last index, because these at defined from BC1 and BC2
    # dc/dr = 0 = (c[1:-1, 1] - c[1:-1, -1])/(2*dr). Means c[1:-1, -1] = c[1:-1, 1]
    # now we must remember that it is cylindrical coordinates! for dcdt
    # diffusion equation part in radial dimension
    # dcdt = D * (d2cdr2 + 1/r * dcdr)
    # discretize it with central difference and set the dcdr is = 0 due to symmetry. 
    # dcdt[:, 0] = D * ((c[:, -1]- 2*c[:, 0] + c[:, 1])/dr**2 + 0)
    # but substitute c[:, -1] with c[:, 1] due to flux = 0 as explained above.
    for i in range(1, Ni):
        
        # ghost point to the left
        C_left = c[i, 1]
        
        # diffusion in z dimension at boundary (nothing special)
        d2cdz2 = (c[i-1, 0] - 2*c[i, 0] + c[i+1, 0])/dz**2
        
        # diffusion in r dimension at boundary, substitute with C_left
        d2cdr2 = (c[i, 1]- 2*c[i, 0] + C_left)/dr**2
        dcdr   = 0
        
        # full governing equation at top boundary
        # dcdt = D * (d2cdz2 + d2cdr2 + 1/r * dcdr)
        dcdt[i, 0] = D *(d2cdz2 + d2cdr2)

    # Upper left corner
    C_top = c[Ni-1, 0] - 2*dz/D * ka * c[Ni,0]  # ghost point in z for Robin BC
    C_left = c[Ni, 1]                           # ghost point in r for symmetry
    d2cdz2 = (c[Ni-1, 0] - 2*c[Ni,0] + C_top) / dz**2      # central difference in z
    d2cdr2 = (C_left - 2*c[Ni,0] + c[Ni,1]) / dr**2        # central difference in r using ghost point
    dcdt[Ni,0] = D * (d2cdz2 + d2cdr2)
    
    # 4. BC at the right (wall)    
    # Robin condition at the side of the wall, where flux is controlled 
    # by the reaction rate.
    # J = -D * dc/dr = ks * c[R]

    # -D * (c[1:-1, Nj+1] - c[1:-1, Nj+1])/(2*dr) = Dks * c[1:-1, Nj]
    # isolate c[1:-1, Nj+1]
    # c[1:-1, Nj+1] = -ks * 2*dr/D * c[1:-1, Nj] + c[1:-1, Nj-1]
    # substitute into central difference approximation of dcdt which is
    # dcdt[1:-1, Nj] = D * ((c[1:-1, Nj-1] - 2*c[1:-1, Nj] + c[1:-1, Nj+1])/dr**2 + 1/r[Nj]*(c[1:-1, Nj+1] - c[1:-1, Nj-1])/(2*dr))) - ks * c[1:-1, Nj]             
    # and substitute c[1:-1, Nj + 1] with C_N_right
    # the reaction is handled through the the robin condition
    for i in range(1, Ni):
        
        # ghost point to the right
        C_right = -ks*2*dr/D * c[i, Nj] + c[i, Nj-1]
        
        # diffusion in z dimension at boundary (nothing special)
        d2cdz2 = (c[i-1, Nj] - 2*c[i, Nj] + c[i+1, Nj])/dz**2
        
        # diffusion in r dimension at boundary, substitute
        d2cdr2 = (c[i, Nj-1] - 2*c[i, Nj] + C_right)/dr**2
        dcdr = (C_right - c[i, Nj-1])/(2*dr)
        
        # full governing PDE at right boundary
        # dcdt = D * (d2cdz2 + d2cdr2 + 1/r * dcdr)
        dcdt[i, Nj] = D * (d2cdz2 + d2cdr2 + 1/r_grid[Nj] * dcdr)
    
    # Upper right corner
    C_right = -ks*2*dr/D * c[Ni, Nj] + c[Ni, Nj-1]   
    C_top = -ka*2*dz/D * c[Ni, Nj] + c[Ni -1, Nj]
    d2cdz2 = (c[Ni-1, Nj] - 2*c[Ni,Nj] + C_top) / dz**2 # robin condition for convection
    d2cdr2 = (c[Ni, Nj-1] - 2*c[Ni,Nj] + C_right)/dr**2 # robin condition for reaction at wall
    dcdr   = (C_right - c[Ni, Nj-1])/(2*dr)
    dcdt[Ni,Nj] = D*(d2cdz2 + d2cdr2 + 1/r_grid[Nj]*dcdr)
    
    #interior points
    for j in range(1, Nj): # excluding last point (boundary). j is index along r dim
        for i in range(1, Ni): # excluding last point (boundary). i is index along z dim
        # dcdt = D * (d2cdz2 + d2cdr2 + 1/r * dcdr)
            d2cdz2 =     (c[i-1,j] - 2 * c[i, j] + c[i+1, j])/dz**2
            d2cdr2 =     (c[i, j-1] -2*c[i, j] + c[i, j+1])/dr**2
            dcdr   =     (c[i, j+1] - c[i, j-1])/(2*dr)  
            dcdt[i, j] = D * (d2cdz2 + d2cdr2 + 1/r_grid[j] * dcdr)
    
    # now we need to flatten it (make it 1D again for solve_ivp)
    dcdt = dcdt.flatten(order = 'F')        
    
    return dcdt

tmax = 60 * 60 * 24 * 1 # 1 day in seconds
sol = solve_ivp(dcdt, [0, tmax], y0 = c0_flat, method='LSODA', 
                t_eval=np.linspace(0, tmax, 100), 
                args=(D, dz, dr, ks, ka, Nr, Nz, r_grid))

# create animation
import matplotlib.animation as animation

fig, ax = plt.subplots()

initial_data = sol.y[:, 0].reshape((Nz, Nr), order='F')
vmin, vmax = sol.y.min(), sol.y.max() 

pcm = ax.pcolormesh(r_grid, z_grid, initial_data, shading='auto',
                    vmin=vmin, vmax=vmax)
fig.colorbar(pcm, ax=ax)
ax.set_xlabel("Radius (m)")
ax.set_ylabel("Height (m)")

def update(i):
    new_data = sol.y[:, i].reshape((Nz, Nr), order='F')
    pcm.set_array(new_data.ravel())
    ax.set_title(f"Time: {sol.t[i]/3600:.2f} h")
    return pcm,

ani = animation.FuncAnimation(fig, update, frames=len(sol.t), interval=50)

plt.show()
