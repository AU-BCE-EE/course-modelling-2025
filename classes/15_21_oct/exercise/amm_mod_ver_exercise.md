# Ammonia volatilization model verification

In this exercise you will work with a version of the ammonia volatilization model from the first mini-project.
This document provides some details, the `amm_concept_model.pdf` has more, and for even more, see the solutions to that mini-project.
Remember that you need to have a good understanding of the underlying conceptual and mathematical models in order to verify a computer model!
So make use of those documents.

You'll use the `dynmod()` function defined in the `amm_mods.py` file in the same subdirectory as this document.
The `amm_mods.py` file is a *module* that defines the model as a Python function called `dynmod()`.
The script `amm_demo.py` has a short demonstration.

The model simulates total ammonia nitrogen (TAN, the sum of free ammonia (NH3) and ammonium (NH4+)) in manure in a storage tank.
It includes continuous addition and removal of manure at a fixed rate, so the volume of manure in the tank does not change.
But TAN is lost through volatilization of ammonia from the surface.

Can you verify the model following the approach we went through in class? 
Save your work in a Python script and a text file, or really in any form that you think is appropriate.
If you prefer commenting in the module file `amm_mods.py` directly, that is fine.

If you struggle to work with the volume-normalized variables and expressions, you can use the second model function `ddynmod()`, named for *double* dynamic model because can also simulation tank volume dynamics.
It does not use volume-normalize values, because the volume is variable over time.
In that case you probably want to set the manure pumping rate (flow) in and out to the same value for simplicity.

For more details on the mass balance and constitutive equations, see `amm_concept_model.pdf`.
