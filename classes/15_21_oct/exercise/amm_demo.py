"""
This is a demonstration of verification of a model from the first mini-project, on ammonia volatilization from stored animal manure.
"""

# Import packages.
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
import amm_mods as am

# To lead new version after edits:
reload(am)

# Reference inputs 
rt = 200 * 86400   # s
depth = 4          # m
kl = 0.01 / 2300   # m/s
c_bg = 0. * 2300   # kg/m3
pH = 7.            
c_TAN_in = 3       # kg/m3
c_urea_in = 0      # kg/m3
ku = 0.            # 1/s

# Reference predictions as demo
pred01 =  am.dynmod(rt = rt,
                    depth = depth,
                    c_TAN_in = c_TAN_in,
                    c_urea_in = c_urea_in,
                    c_TAN_0 = c_TAN_in,
                    c_urea_0 = c_urea_in,
                    c_bg = c_bg,
                    pH = pH,
                    ku = ku,
                    kl = kl,
                    times = np.arange(0, 365 * 86400, 30 * 86400)
)

# What does output look like?
pred01

```{python}
plt.close()
plt.plot(pred01['t'] / 86400, pred01['tan'])
plt.ylim(0, 3.1)
plt.xlabel('Time (d)')
plt.ylabel('Tank TAN conc. (kg/m3)')
#plt.show()
plt.savefig('demo_preds_01.png')
```

# You will need to change some input parameters for verification
# Change to initial TAN concentration of 0, for example

pred02 =  am.dynmod(rt = rt,
                    depth = depth,
                    c_TAN_in = c_TAN_in,
                    c_urea_in = c_urea_in,
                    c_TAN_0 = 0.,
                    c_urea_0 = c_urea_in,
                    c_bg = c_bg,
                    pH = pH,
                    ku = ku,
                    kl = kl,
                    times = np.arange(0, 365 * 86400, 30 * 86400)
)

pred02

plt.close()
plt.plot(pred02['t'] / 86400, pred02['tan'])
plt.ylim(0, 3.1)
plt.xlabel('Time (d)')
plt.ylabel('Tank TAN conc. (kg/m3)')
#plt.show()
plt.savefig('demo_preds_02.png')
