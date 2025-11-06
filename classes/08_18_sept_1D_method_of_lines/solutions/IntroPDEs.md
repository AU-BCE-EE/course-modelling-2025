### Exercise solutions - Introduction to PDEs

1.  In a plug-flow reactor cis-2-butene is converted to trans-2-butene with first order reaction kinetics. The direction of the liquid flow is along the z-axis, but molecules also move in the radial direction (along the r-axis) due to diffusion. Write the transport equation in cylindrical coordinates assuming that there is no angular variation.

Solution: Looking at the Appendix A in Rasmuson et al. 2014. We can see the mass balance for component A and remove all terms that involves theta. We can also remove advection along the r-axis.

$$\frac{\partial C_A}{\partial t} = -v_z \frac{\partial C_A}{\partial z} + D \left[\frac{1}{r} \frac{\partial}{\partial r} \left( r \frac{\partial C_A}{\partial r} \right) + \frac{\partial^2 C_A}{\partial z^2}
         \right]+ R_A$$

2.  You have a large room with people and somebody slips a fart in the middle of the room releasing a limited amount of $H_2S$. The $H_2S$ spreads slowly to the rest of the room.

Solution: We choose rectangular coordinates, since it is within room (normally rectangular). There is no bulk flow (advection) only diffusion (hint: "spreads slowly"). Crossing out advection terms and realizing we have three dimensions in a room we get:

$$
\frac{\partial C_A}{\partial t} = D \left(\frac{\partial^2 C_A}{\partial x^2} + \frac{\partial^2 C_A}{\partial y^2} + \frac{\partial^2 C_A}{\partial z^2} \right)
$$

3.  You are given the following PDE: $\frac{\partial C_A}{\partial t} = -v \frac{\partial C_A}{\partial x}$

Can you come up with some examples of what this model could represent? What assumptions do you need to make?

Solution: The model only describes advection. This suggest that diffusion is not important. And since it is a 1D model, the advection probably occurs along a long pipe, where advection in other directions are not occurring. Since diffusion is relatively quick in gases, then the model might represent reactant A being in a liquid phase. There is no reaction either, so C~A~ could be an inert species like salt in water. It could for instance be describing salt water running through a pipe at a relatively fast flow rate. But it could also represent many other things...
