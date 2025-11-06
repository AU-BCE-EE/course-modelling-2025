# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 09:07:09 2025

@author: au277187
"""

fig, ax = plt.subplots()
vmin, vmax = sol.y.min(), sol.y.max()
pcm = ax.imshow(sol.y[:,0].reshape((Nx, Ny), order='F'),
                vmin=vmin, vmax=vmax,
                origin='lower', extent=[0,Lx,0,Ly],
                aspect='equal', cmap='hot')

cbar = fig.colorbar(pcm, ax=ax)
cbar.ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
cbar.ax.yaxis.get_offset_text().set_visible(False)

ax.plot(Lx/2, Ly/2, 'bo', label='Center')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.legend()

def update(frame):
    T_frame = sol.y[:, frame].reshape((Nx, Ny), order='F')
    pcm.set_data(T_frame)
    ax.set_title(f"Time: {sol.t[frame]:.1f} s")
    return [pcm]

ani = animation.FuncAnimation(fig, update, frames=len(sol.t), interval=500, blit=True)
plt.show()


# Print center temperature over time
center_idx = (Nx//2) + (Ny//2)*Nx
T_center = sol.y[center_idx, :]
import matplotlib.pyplot as plt
plt.figure()
plt.plot(sol.t, T_center)
plt.xlabel('Time [s]')
plt.ylabel('Center Temperature [°C]')
plt.grid(True)
plt.show()