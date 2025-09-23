1.  Identify from the problem text where information is given about the boundary conditions and initial conditions. What type of BCs would be good to use? Try to formulate the BCs and ICs for each problem.

A)  Oxygen diffuses into your cell tissue at your forehead while your cycling. The wind is blowing and constantly refreshing the air at the surface of your forehead. By sticking a micro oxygen sensor into your cell tissue on your forehead you notice that the concentration of oxygen drops and then increases again until you hit a capillary arteria, which is saturated with oxygen.

B)  You are designing a drug delivery system where a biodegradable polymer implant releases medication into surrounding tissue. The implant is embedded inside a muscle, and the drug diffuses outward through the muscle tissue. At the surface of the implant, the drug is released at a constant rate controlled by the degradation of the polymer. Far away from the implant, at a certain distance, the tissue type changes and the drug cannot pass that tissue barrier.

C)  You have a long metal rod heated at one end by an electric heater that maintains the rod tip at a constant temperature. The other end of the rod is insulated so that no heat can escape from that side. Over time, heat diffuses through the rod, and you want to analyse the temperature distribution inside the rod.

D)  A hot metal sphere is suddenly immersed in a large water bath maintained at a constant temperature. The sphere cools down by losing heat through its surface by convection to the surround water. The temperature inside the sphere changes with time as heat diffuses radially from the center to the surface, and the heat flux at the surface depends on the difference between the sphere's surface temperature and the water temperature.

2.  Try to set up this mathematical model in python 
$$\frac{\partial C_A}{\partial t} = -v \frac{\partial C_A}{\partial x}$$

How many boundary conditions and initial conditions do you need? Use a Dirichlet BC and solve it with method of lines in python. For discretization of the first derivative try: central difference and backward difference, which is better?

3.  Construct a model that predicts the temperature along a 10 m long insulated copper wire over time and space. In one end of the wire a heat source provides enough energy to ensure that the temperature is maintained at 200 degree C, the other end is open to the surrounding air outside.

4.  A 2 m long plug flow reactor converts 100% O2 gas into CO2 gas by providing some carbon source inside the reactor. The reaction rate follows first order kinetics with k = 0.01 minute-1. Construct a model that predicts the concentration of O2 along the plug flow reactor. Choose reasonable values for your model variables and use it to estimate approximately the minimum flow rate needed to reach O2 concentration in the outlet of 5% at a steady state. How long time does the reactor need to run before a steady-state is reached?

5.  A sphere of iron has to be cooled in a water bath. Construct and solve a model in python to predict the temperature of the sphere. Consider first what coordinates you want to use and what assumption you can make about symmetry. Define your own initial and boundary conditions from what you think is realistic and clearly state your assumptions. The model should be able to predict the temperature of the sphere over time and distance from the center of the sphere.

6.  Last exercise is a bit difficult: You want to transfer an aqueous solution of acetate with a concentration of 10 g/m3 to a reactor. Before the reactor the solution has to go through a 2 m long pipe that is already filled with water contaminated with 1 g bacteria/m3. You need a flow velocity of 1 m/d in the pipe and you are concerned whether the bacteria will eat all the acetate before it reaches the reactor. Construct a model that predicts concentrations of acetate and bacteria along the pipe and over time. The bacteria follows Monod kinetics with a umax of 0.5 pr hour and a half saturation constant (Ks) of 0.2 g acetate/m3. The biomass yield of the bacteria (Y) is 0.5 g biomass pr g acetate consumed.   