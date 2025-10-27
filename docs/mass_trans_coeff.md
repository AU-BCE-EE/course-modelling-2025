# Some information on *inter-phase* mass transfer coefficients 

There are various *correlations* that can be used to estimate mass transfer coefficients.
These "correlations" are equations that relate mass transfer coefficient value to dimensionless variables like the Reynold's number, which in turn are calculated from system dimensions and other properties. 
Cussler (2009) has a couple tables with popular correlations in Chapter 8.
For flow that is smooth and not turbulent, i.e., laminar flow, correlations have been developed by theory.
But for more common turbulent flow, correlations are empirical, i.e., based on measurements.

So, what numeric values might you use?
For flow over a flat surface ("flat plate" in mass transfer terminology) and wind speeds between 0.5 and 2 m/s, correlations predict an air-side mass transfer coefficient between 0.001 and 0.01 m/s.
These values are for concentration differences expressed in gas phase units.

For mass transfer from one fluid to another where resistance is present in both phases, we need to combine the mass transfer coefficients from the two.
This can be done using Henry's law constant or an analogous partition coefficient.
But in many cases it is possible to assume that one phase dominates resistance.
For mass transfer from a water solution to air, for example, volatilization of highly soluble compounds tends to be limited by air-side resistance, because there is a high concentration of solute within the water.
So even if the solute were somehow depleted close to the interface, a high concentration would drive a high flux to replenish it.
This approach is commonly taken with ammonia, for better or worse.

So something around 0.001 and 0.01 m/s would be appropriate for the ammonia model, but remember that these values refer to gas phase units!
That is, the "hidden" concentration difference in those values is for a gas phase concentration.
What 0.01 m/s actually means in this case is a flux of 0.01 kg/m2-s per gas phase concentration difference of 1 kg/m3.
But the kg cancel out and when you combine the 1/m2 with 1 / (1/m3) you end up with m on the top.

It is essential that the mass transfer coefficient phase matches the concentration difference phase.
You absolutely cannot use a mass transfer coefficient in gas phase units directly with an aqueous concentration difference!
But you could convert the phase of either the concentration difference or the coefficient so they match.

An approximate value of Henry's law constant for ammonia around ambient temperature is 2300 (aq:g).
This is a value for a unitless form, as an aqueous-to-gas phase ratio, which is why we write aq:g after the value (although this is often omitted in publications).
So it means that at equilibrium, the ratio of aqueous concentration to gas concentration *in the same units* is 2300.
So if the gas phase concentration was 1 g/m3, the equilibrium aqueous concentration would be 2300 g/m3, or 2.3 g/L, which is quite high for NH3, because this is the concentration of the uncharged NH3 (aq) species, not including NH4+.

But back to a numeric value for Henry's law constant.
Assuming 0.01 m/s for gas phase units, the aqueous phase value would be:

```
0.01 m/s (1/gas) / 2300 (aq/gas)
```

which equals `4.3E-6` m/s.
I have added the phase above so you can see how the `gas` phase cancels and you end up with `(1/aq)` in the final unit.
It can help to explicitly write the concentration units in both the mass transfer coefficient and Henry's law constant.

```
0.01 kg/m2-s             2300 kg/m3 (aq)        4.3E-6 kg/m2-s
----------------  /     ----------------  =    ---------------   = 4.3E-6 m/s
1 kg/m3 (gas)              1 kg/m3 (g)             1 kg/m3 (aq)
```

And, in your Python code, it can help to explicitly write `0.01 / 2300` to help remember that you are converting a mass transfer coefficient that refers to gas phase units to one for aqueous phase units.

