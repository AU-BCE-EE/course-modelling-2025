import numpy as np 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# diffusion in an open pipe with 10 mg/m3 in left side to start with
#  ----------------------------------
# 10  0  0  0  0  0  0  0  0  0  0  0                                  
#  ----------------------------------
# 
# dc/dt = D * d2c/dx2

D = 0.00002 # m^2/s
L = 1 # meter
dx = 0.01 # meter
x_grid = np.arange(0, L+ dx, dx)
tmax = 1000 # max time, s

def rates(t, c, dx, x_grid):
    
    dcdt = np.zeros(len(x_grid))
    N = len(x_grid)-1
       
    for i in range(1, N):
        dcdt[i] = D * (c[i-1] - 2 * c[i] + c[i+1])/dx**2
    
    return dcdt

c0 = np.zeros(len(x_grid))
c0[0] = 10

tmax = 1000 # s
sol = solve_ivp(rates, t_span = [0, tmax], y0 = c0, method = 'LSODA',
                t_eval = np.linspace(0, tmax, 1000),
                args = (dx, x_grid))
  
for i in range(0, len(x_grid)-1, int((len(x_grid)-1)/5)):
    plt.plot(sol.t, sol.y[i], label = f'{i*dx} m')
plt.legend(loc = 1)
plt.ylabel('concentration, mg/m3')
plt.xlabel('time, s')

# How much O2 has diffused in and out of the model domain?
# flux into model domaim: J = -D * dc/dx
# J = -D * (c[i+1] - c[i])/dx: J = -D * (c[1] - c[0])/dx
c_0 = sol.y[0, :]
c_1 = sol.y[1, :]

flux_in = -D * (c_1-c_0)/dx # unit is mg/m2/s

# flux out of domain: 
# J = -D * (c[i+1] - c[i])/dx
cN = sol.y[-1, :]
cN2 = sol.y[-2, :]

flux_out = -D * (cN - cN2)/dx

time = sol.t
plt.plot(time, flux_in, label = "flux_in")
plt.plot(time, flux_out, label = "flux_out")
plt.legend(loc = 1)
plt.xlabel('time, s')
plt.ylabel('mg/m2/s')

flux_in_cum = np.trapz(flux_in, sol.t)
flux_out_cum = np.trapz(flux_out, sol.t)

net_flux_cum = flux_in_cum - flux_out_cum
print(net_flux_cum)
total_O2_end = np.trapz(sol.y[:, -1], x_grid)
print(total_O2_end)

print(c0)
initial_C = c0[0] * dx/2
print(total_O2_end - initial_C)


def rates2(t, c, dx, x_grid, c_left, c_right):
    
    dcdt = np.zeros(len(x_grid))
    N = len(x_grid)-1
    
    dcdt[0] = D * (c_left - 2*c[0] + c[1])/dx**2
    dcdt[-1] = D * (c[-2] - 2*c[-1] + c_right)/dx**2
    
    for i in range(1, N):
        dcdt[i] = D * (c[i-1] - 2 * c[i] + c[i+1])/dx**2
    
    return dcdt

c0 = np.zeros(len(x_grid))
c_left = 10
c_right = 0

tmax = 1000 # s
sol2 = solve_ivp(rates2, t_span = [0, tmax], y0 = c0, method = 'LSODA',
                t_eval = np.linspace(0, tmax, 1000),
                args = (dx, x_grid, c_left, c_right))

# flux = J = -D * (c[i+1] - c[i-1])/(2*dx)
c_1 = sol2.y[1, :]
flux_in = -D * (c_1 - c_left)/(2*dx) # unit is mg/m2/s

# flux out of domain: 
# J = -D * (c[i+1] - c[i])/dx
cN2 = sol2.y[-2, :]
flux_out = -D * (c_right - cN2)/(2*dx)

flux_in_cum = np.trapz(flux_in, sol2.t)
flux_out_cum = np.trapz(flux_out, sol2.t)

net_flux_cum = flux_in_cum - flux_out_cum
total_O2_end = np.trapz(sol2.y[:, -1], x_grid)

print(net_flux_cum)
print(total_O2_end)

plt.plot(flux_out)

initial_C = c0[0] * dx/2
print(total_O2_end - initial_C)
