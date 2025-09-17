Exercises - Method of lines

1.  Discretize the following PDEs with method of lines approach.

A)  1D advection
$$\frac{\partial u}{\partial t} + c \frac{\partial u}{\partial x} = 0$$

B)  2D diffusion 
$$\frac{\partial u}{\partial t} = D \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

C)  1D advection-diffusion 
$$\frac{\partial u}{\partial t} = D \frac{\partial^2 u}{\partial x^2} - c \frac{\partial u}{\partial x}$$


2. You watched a video at home dealing with diffusion in a pipe. You can download the code from the video in the "demos" folder to this class and try to use it on your own PC if you did not make it from home. The script is also a good place to build from in future exercises..

A) In the video there was no mention of the boundary conditions, but the problem cannot be solved without boundary conditions. 

Try to identify what the boundary conditions actually were?

B) Try to change the space step size (dx) to larger or smaller numbers. Does this change the solution?