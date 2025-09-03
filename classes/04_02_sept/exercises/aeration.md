# Aeration

Water can be aerated (or more accurately, oxygenated) by introducing a continuous flow of air bubbles at the bottom of a tank or other vessel.
Mass transfer rate depends on the mass transfer coefficient $k_L$ ($\text{m} \text{s}^{-1}$) and the bubble area $A$ ($\text{m}^2$) which is typically expressed on a volumetric basis as $a$ (so $\text{m}^2 \text{m}^{-3}$).
These two are typically combined into a single, observable, parameter called $k_La$ ($\text{s}^{-1}$ or actually commonly $\text{h}^{-1}$).

A wastewater treatment tank is aerated in this way and the $k_La$ is around 20 $\text{h}^{-1}$.
Formulate a model for the change in dissolved oxygen concentration over time given completely anaerobic water.

You may find it helpful to assume that the tank has a uniform dissolved oxygen concentration at any time.

Once you have a governing equation for your model, try to implement it in Python.
First, try to solve it using Euler's method.
Then, try to develop an analytical solution.
Compare the two.
