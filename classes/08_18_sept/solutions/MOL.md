### Exercises - Method of lines

1.  Discretize the following PDEs with method of lines approach.

A\) 1D advection

$$\frac{\partial c}{\partial t} + v \frac{\partial c}{\partial x} = 0$$

Solution: With central difference formula for du/dx we get.

$$
\frac{\partial c}{\partial t} + v\frac{c_{i+1}-c_{i-1}}{2\Delta x} = 0
$$

B\) 2D diffusion

$$
\frac{\partial c}{\partial t} = D \left( \frac{\partial^2 c}{\partial x^2} + \frac{\partial^2 c}{\partial y^2} \right)
$$

Solution: With central difference formula for
d<sup>2</sup>u/dx<sup>2</sup> and d<sup>2</sup>u/dy<sup>2</sup> we get.

$$
    \frac{\partial c}{\partial t}
    = D\left(
    \frac{c_{i-1,j}-2c_{i,j}+c_{i+1,j}}{\Delta x^2}
    +
    \frac{c_{i,j-1}-2c_{i,j}+c_{i,j+1}}{\Delta y^2}
    \right)
$$

C\) 1D advection-diffusion

$$
    \frac{\partial c}{\partial t} = D \frac{\partial^2 c}{\partial x^2} - v \frac{\partial c}{\partial x}
$$

Solution:

$$
    \frac{\partial c}{\partial t}
    = D\left(\frac{c_{i-1}-2c_i+c_{i+1}}{\Delta x^2}\right)
    - v\left(\frac{c_{i+1}-c_{i-1}}{2\Delta x}\right).
$$


2. You watched a video at home dealing with diffusion in a pipe. You can download the code from the video in the "demos" folder to this class on GitHub and try to use it on your own PC if you did not make it from home. 
The script is also a good place to build from in future exercises..

A\) In the video there was no mention of the boundary conditions, but the problem cannot be solved without boundary conditions. 

Try to identify what and how the boundary conditions were actually set?

Solution: Notice that dcdt is initiated as zeros in the `rates()` function and since in the for loop we are only affecting interior nodes, then `dcdt[0]` (left boundary) and `dcdt[N]` (right boundary)
stays as 0 for all times. if dcdt = 0 at the boundaries then the state variable cannot change! Therefore by "doing nothing" we actually enforce that the values at the boundaries are not changing and stays as we defined them in the initial conditions (10 and 0).
This is called Dirichlet type BCs in both ends. However, a better practice is to explicitely write `dcdt[0] = 0` and `dcdt[N] = 0` in the `rates()` function for safety. 

B\) Try to change the space step size (dx) to larger or smaller numbers. Does this change the solution? Why could that be?

Solution: Yes there is a small change in the profile, which result mainly from higher numerical precision with smaller dx. We are lucky that this is a Dirichlet boundary condition, because the result is not much affected in that case. 
The implications could be much worse if we used other boundary conditions and here it is not only the numerical precision that is a problem. In that case we need to scale the initial concentration to the size of each cell. So in that case it is better to think of an initial mass, and from that initial mass we compute the concentration depending on the size of the cells.




