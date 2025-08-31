# Water tank exercise

Here is a simple exercise that will still require the typical steps in model formulation to reach a solution.
Assume you have a big water cubic tank, say 10 $\text{m}^3$, that is draining from a horizontal pipe out of the bottom under the force of gravity.
You measure an initial flow rate of 100 $\text{L}~\text{min}^{-1}$ when the tank is full.
If you assume that flow rate is proportional to the tank pressure, which is not an unreasonable assumption (but not always true), then it is also proportional to the quantity of water remaining in the tank.
So can you develop an analytical model to calculate the volume of water remaining in the tank at any time?

Here is the steps we've discussed for model formulation.
1. Initial concepts and assumptions (boundary, state variables, sketches)
2. Balance/conservation equations
3. Constitutive equations (transfer or rate equations)
4. Linking equations
5. Spatial or other simplifications
6. Initial or boundary conditions
7. Governing equation
8. Analytical or numerical solution

And here are some hints that correspond to the steps above.
1. The boundary should be very simple.
2. Most of the typical terms in the water mass or volume balance equation are zero.
3. There is one, very simple, empirical constitutive equation.
4. No linkage equation is needed.
5. Spatial? No need to think about it.
6. You know the initial water volume.
7. Combine the balance and constitutive equation to get a governing equation--an ODE for the rate of change in water volume.
8. And then integrate it analytically.
