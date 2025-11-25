# Parameter estimation exercise

This exercise is based on the model from the second mini-project.
You can load the model function from the `O2dc_mods` module included in this directory.
The model function is `O2dc()` and you can find a demo in the [class 19 solution directory](https://github.com/AU-BCE-EE/course-modelling-2025/blob/main/classes/19_04_nov_mini_project2/solution/demo.py).
Work through the demo if needed to understand inputs and outputs.

The 1D model was developed for diffusion-controlled oxygen and organic matter (OM) transport in a wastewater polishing lagoon.
However, it may be reasonable to apply to model to cases where transport is enhanced by mixing, as long as most of the resistance to transport remains in the water column (not the air)and the mass transfer parameter `D` is not too large.

Measurements are available from a 1 m deep lagoon and will be used for parameter estimation. 
The wastewater initially had a degradable organic matter (OM) concentration of 10 mg/L, initial oxygen 8 mg/L, and the system is run in batch mode. 
The file `meas_O2.csv` has measurements of dissolved oxygen concentration at the bottom of the lagoon at a daily frequency.
The concentration of OM in a sample from around 50 cm deep is in the file `meas_OM.csv` at a roughly 1 week frequency.
These measurements are made up, but could reflect the ease of making electrode-based measurements of dissolved oxygen and a more complicated analysis for OM (e.g., biochemical oxygen demand (BOD) incubation).

1. Assuming a reaction rate around 1E-4 m3/kg-s and that mass transfer is completely diffusion-controlled (see `parameter_values.md` if you need help coming up with a value), carry out a graphical validation of the model for both oxygen and OM.
Come up with a hypothsis for any differences you observe between measurements and model output.

2. Use `least_squares()` to estimate values for the (apparent) diffusivity and reaction rate (two parameters) based on the oxygen measurements.
It might be a good idea to change the model function so it accepts arbitrary times instead of `tmax` and `nt`.

3. Repeat the process, but this time use the OM concentrations.
Compare to the previous estimates.

4. Optional: Use both sets of measurements simultaneously for parameter estimation and compare the estimated values to what you got above. 
Use weights to ensure that each of the observed variables contributes equally to the parameter estimates, considering the lower sampling frequency of the OM measurements.
Check out the `loss` parameter for the `least_squares()` function and try a setting that minimized the influence of outliers (extreme values).
Do the parameter estimates change much?

5. Optional: What values would you ultimately recommend for these parameters based on the available measurements?
Are these results consistent with your hypothesis from 1?

## Some tips
* Remember to try different starting values.
* Do you need different values for `D` for the two solutes?
* Use `print()` calls in your residuals function to see what the values of the parameter guesses (or residuals) are if you encounter problems.
* If you ever see (or suspect) the completely implausible or impossible parameter guesses are causing problems, check out the `bounds` parameter (argument) in the `least_squares()` help file.
