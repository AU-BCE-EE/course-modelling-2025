# Residence time function demo
Sasha D. Hafner

# Overview

This is a simple Python simulation of some arbitrary pool with discrete
particles flowing in and out. It is meant to explore the concept of
residence time and show effects of unequal inflow and outflow.

# Packages

``` python
import numpy as np
```

# The simulation function

``` python
def rtsim(p0, r_in, r_out, dt, time):
  
  # Create initial pool of particles
  p = np.zeros(int(p0))
  
  # Number of time steps
  n = int(time // dt)
  
  # Loop through times
  for _ in range(n):
    # Update age of all particles in pool
    p += dt
    # Select random particles for keeping in pool
    p = np.random.choice(p, size = p.size - int(r_out * dt), replace = False)
    # Add new particles to pool, all with age 0
    p = np.concatenate((p, np.zeros(int(r_in * dt))))
    
  return p
```

# Application

1.  Pool of 10,000 with flow rate in = flow rate out = 100.

``` python
out = rtsim(1E4, 100, 100, 1, 1000)
np.mean(out)
```

    98.1758

1.  Increase flow.

``` python
out = rtsim(1E4, 200, 200, 1, 1000)
np.mean(out)
```

    49.3689

1.  Decrease flow

``` python
out = rtsim(1E4, 10, 10, 1, 1000)
np.mean(out)
```

    629.9369

``` python
out.size
```

    10000

1.  Flow in \> flow out (pool size grows)

``` python
out = rtsim(1E4, 102, 100, 1, 1000)
np.mean(out)
```

    114.50941666666667

``` python
out.size
```

    12000

``` python
out.size / 102
```

    117.6470588235294

``` python
out.size / 100
```

    120.0

1.  Flow out \> flow in

``` python
out = rtsim(1E4, 100, 102, 1, 1000)
```

``` python
np.mean(out)
```

    80.82625

``` python
out.size / 102
```

    78.43137254901961

``` python
out.size / 100
```

    80.0
