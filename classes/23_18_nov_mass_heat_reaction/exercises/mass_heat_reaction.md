Exercises - Coupled mass and heat transfer

1.  Decomposition of $2H_{2}O_{2} \rightarrow 2H_{2}O + O_{2}$ is an exothermic reaction that occurs in water. The reaction takes place in a batch reactor and follows first order kinetics. The rate constant is temperature dependent like this:

$$k(T) = A \times exp(-\frac{E_{a}}{RT})$$

The batch reactor is cooled by a cooling jacket with ambient water temperature $T_c$ of 20 deg C. The surface area between the cooling jacket and the reactor is 1 $m^2$. A stirrer ensures that the reactor is perfectly mixed.

$$
E_{a} = 8 \times 10^{4} \; J/mol
$$ 

$$
A = 1 \times 10^{10} \; s^{-1}
$$ 

$$
R = 8.314\ \mathrm{J/(mol \cdot K)}
$$ 

$$
\Delta H_{rxn} = -98 \cdot 10^3\ \mathrm{J/mol}
$$

$$
C_{p,water}= 4180\ \mathrm{J/(L \cdot K)}
$$

$$
\rho = 1000 \; kg/m^{3} 
$$

$$
q_{stirrer} = 5000 \; J/(s \cdot m^{3})
$$

$$
T_{0} = 293 \; K
$$

The reactor working volume is 100 L and with an initial concentration of 1 mol/L of $H_{2}O_{2}$ in an aqueous solution. The heat from the reactor is removed with an overall heat transfer coefficient of 

$$
U = 50\; J/(s \cdot m^{2} \cdot K)
$$

A\)  Write the heat and mass balance for the reactor.

B\)  Setup the model in python and try to run it. The reaction product should not exceed 305 K. Try to accomplish that by adjusting the overall heat transfer coefficient (U). How could the over all heat transfer coefficient be increased in practice?

C\)  There is no reason to keep the stirrer running after the reaction is complete. Implement code that turns of the stirrer after the reaction is 99% complete. Does it have any effect on the temperature?

D\)  Try to add the products to the rates function as well and plot it together with the reactant

E\) Consider how you could change this problem (in part A and B) into a 1D model?

F\) Difficult exercise: Expand your 0D model to a 1D model. You can assume the following. The model will include the horizontal dimension in the reactor and with heat transfer through the side walls due to the cooling jacket. Keep the parameters from the 0D exercise. The diameter of the tank is 0.5 meter and still contains only 100 L working volume. The initial concentration everywhere is similar to the 0D problem (1 mole/L). 
