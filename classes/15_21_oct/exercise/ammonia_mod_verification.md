# Ammonia volatilization model verification

Take a look at a model of ammonia volatilization from stored animal manure that is taken from a solution to the first mini-project.
The `amm_mods.py` file is a *module* that defines the model as a Python function called `dynmod()`.
The script `amm_demo.py` shows has a short demonstration.

The model simulates total ammonia nitrogen (TAN, the sum of free ammonia (NH3) and ammonium (NH4+)) in manure in a storage tank.
It includes continuous addition and removal of manure at a fixed rate, so the volume of manure in the tank does not change.
But TAN is lost through volatilization of ammonia from the surface.

The mass balance for this system for TAN is:

```
TAN accumulation = TAN pumping in - NH3 volatilization out + TAN generation - TAN pumping out
```

where all terms are kg/m3-s (N mass normalized to tank volume).

And for urea:

```
Urea accumulation = Urea pumping in - urea hydrolysis - urea pumping out
```

These terms are also as N mass per m3 tank volume per s (kg/m3-s).

Volatilization rate in kg/s should be:

```
k_l * A * (f_NH3 * c_TAN,tank - c_NH3,bg / H)
```

where `k_l` is the liquid phase unit mass transfer coefficient (m/s), `f_NH3` is the fraction of TAN present as the free ammonia species NH3, `c_TAN,tank` is the TAN concentration in the tank (kg/m3), `c_NH3,bg` is NH3 (g) concentration in the air (the background concentration), and `H` is a unitless version of Henry's law constant as aqueous to gas or aq:g (i.e., (kg NH3 per m3 in manure) per (kg NH3 per m3 in air)).
Tank area is `A` (m2).

Normalizing by tank volume means simply dividing the above expression by tank volume.
And tank area divided by tank volume is tank depth `d`, assuming a cylindrical or rectangular tank.
So, we have:

```
NH3 volatilization out = k_l / d * (f_NH3 * c_TAN,tank - c_NH3,bg / H)
```

Can you verify the model following the approach we went through in class? 
Save your work in a Python script and a text file, or really in any form that you think is appropriate.

If you struggle to work with the volume-normalized variables and expressions, you can use the second model function `ddynmod()`, named for *double* dynamic model because can also simulation tank volume dynamics.
It does not use volume-normalize values, because the volume is variable over time.
In that case you probably want to set the manure pumping rate (flow) in and out to the same value for simplicity.
