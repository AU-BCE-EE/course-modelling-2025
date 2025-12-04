# The modelling lingo glossary
Rasmus Danneskjold Koldtoft Pedersen

## Boundary conditions
Boundary conditions are specific rules which pertain to the boundary in question. 
An example would be a pool of water exposed to the air where the boundary is at the surface of the water. 
In this case the water would interact with the surrounding air whether it was cooled down or in equilibrium with oxygen. 
IF you go an infinitesimal distance down into the water you now won't have the direct interaction with air but only with the surrounding water. 
Therefore the conditions which are present for the water at the boundary are fundamentally different than those of the inner domain (see "domain") points.

### Dirichlet boundary conditions
A Dirichlet boundary condition fixes the value of a parameter at the boundary meaning $u(x\ at\ boundary)=u_{constant}$. 
It is used when the physical implications of the boundary condition can be approximated as constant, such as a fixed temperature from a heater or oxygen concentration at the surface water body.

### Neumann boundary conditions
A Neumann boundary condition specifies the derivative of the function at the boundary rather than the value itself. 
This kind of boundary condition is utilized when the change at the boundary is known rather than the value which is often the case for flux-based boundaries. 
If no flux occur, we have $\frac{du}{dn}=0$ which we see with insulators or with closed walls or if some flux occur, we have $\frac{du}{dn}\neq 0$.
Both are Neumann boundary conditions, but they describe different scenarios.

### Robin boundary conditions
Robin boundary conditions specifies a linear combination of a given function and the derivative observed at the boundary. 
In another term it is a mix of Dirichlet and Neuman Boundary conditions, $a\dot u + b \frac{du}{dn} = c$. 
An example of a Robin boundary condition could be Newtons law of cooling at the boundary between a hot mass and the air surrounding it.
$-k \frac{dT}{dx} = h(T_{\infty} - T_S)$ can be rearranged to $hT_S - k \frac{dT}{dx} = hT_{\infty}$ has as the variable instead of and all the other constant components such as *k*, *h* and $T_{\infty}$.

*In all examples given in the above boundary condition equations the derivatives are always given by "n". 
"n" is simply the direction normal (perpendicular) to the boundary. 
In a 1D model*
$\frac{\partial}{\partial n}$ *simply becomes*
$\frac{\partial}{\partial x}$. 
*This entails that the flux/movement through the boundary is always normal to the boundary itself and is also a way to visualize when we are looking at boundary equations vs normal equations.*

## Conservation laws
The conservation laws are a fundamental principle in physics stating that a physical property within an isolated system remains constant over time. 
This applies to energy, mass, momentum etc. 
Nothing can in principle be created nor destroyed, only converted. 
In engineering we often utilize mass balances to describe this phenomenon, meaning if we put a total of 1 kg of mass within a system, we will regain 1 kg of mass from the system in some way shape or form. 
In project 2 you applied the conservation laws when checking the solution using the "np.trapz()" function.

## Discretization
Discretization is the act of taking something continuous and describing it with a finite set of points (or "nodes" or "cells"). 
It is used widely in the world of computation simply because it is fundamentally impossible for a computer to handle continuous data/information. 
Also depending on how much you discretize a given domain (see "domain") you can vary computational time i.e. solving a governing equation for 5 points takes less time than for 500 points, however the 5-point solution would typically  be less accurate than the 500-point solution. 
So all in all it is a question between quality and quantity. 
You have learned about forward, backward and central differences, which are methods of discretizing derivatives.

## Distributed parameters
A system with distributed parameters have those parameters vary over space and time. 
An example of such is a cup of coffee. 
The liquid has conductive properties which are different to those of the mug wall meaning that the conductive parameters are different throughout the
domain (see "domain").
However, this exact system might be modeled with a lumped parameter approach!

## Domain
The volume or area of the simulated physical system included in the model. 
If a glass of water is considered,
where are the boundaries located? 1. At the water edge inside of the
glass? 2. At the glass wall outside? 3. Or "x" cm from the glass wall?
Each domain example yields in different considerations. For the first
(1) example the boundary would be between the water and glass material
with anything beyond the glass being neglected (basically
non-interactive with the study - see "study"). For the second (2)
example the boundary would be between the glass and surrounding air
which (in most cases when defined like this) considers the air a
constant physical influence AND includes the glass material which is
important fx in heat conduction analysis. The third (3) scenario
considers a layer of air surrounding the glass surface and how there
might be a gradient through it (fx in regard to temperature). In reality
EVERYTHING should be considered, to be most accurate HOWEVER this is not
feasible, and it is therefore up to the student where to draw the line.

## Dynamic/transient system
When a system is dynamic or transient it is constantly changing with
time meaning . Set a simple chemical reaction A B as an example. If the
concentration of A changes with time, so is the reaction environment
meaning the reaction conditions change as time goes by. If we assume a
total conversion of A to B we often see an exponentially decreasing
curve as a function of time for species A. As the curve flattens out it
is said to reach steady state since (see "steady state"). An
often-utilized description of the steady state point for cases such as
this is when 99% of (convertible) A is converted. See also the Rasmuson
et al. Chapter 2 on classification.

## Empirical
The word empirical refers to things which are practically determined
rather than theoretically derived. An example of such is the Arrhenius
equation, $k = A exp(-\frac{Ea}{RT})$, where *A* is an empirically
derived parameter. Empirical values are thereby not possible to
"calculate" and if required they are often found in various tables in
literature often presented as varying with temperature, pressure etc.

## Finite difference method
The finite different method is a method to approximate derivatives by
replacing the derivative term with differences between two neighboring
points on a discretized grid (see "discretization"). Usually a finer
discretization (more grid points) yield in more accurate solutions
however this also takes up more computation time/power. Although an
approximation and thereby less accurate it allows us to convert the
differential equation into algebraic equations which can be solved
numerically by using algorithms such as Euler, backwards Euler,
Runge-Kutta etc.

## Governing equation
The governing equation is the main equation which explains the physical
phenomena observed in our study (see "study). It could be Ficks law in
mass transfer, Fourier's law in heat conduction or Navier-Stokes
equation in bulk flow [1]. It is NOT TO BE CONFUSED with boundary
conditions (see "boundary conditions") or linking equations (see
"linking equations"). In this course we did not learn about
Navier-Stokes, but it is central to more advanced modelling.

[1] <https://www.youtube.com/watch?v=8wXWEsHR47A>

## Indexing (slicing)
Indexing is a term which describes the act of accessing, setting, or replacing discrete (see
discretizing) points within a given domain. You can discretize a PFR up
in 100 sections with indexing describing the individual points and the
information stored in each point after solving the model. An example of
indexing and how it fundamentally differs to discretizing is a chess
board. It is essentially a 2D square discretized in 8 rows and 8
columns. Indexing is then the act of accessing each square ie A1, A2,
B1, B2 etc [2].

[2]
<https://en.wikipedia.org/wiki/Chessboard#/media/File:Modern_Fianchetto_Setup._Chess_game_Staunton_No._6.jpg>

## Initial conditions
Initial conditions are conditions/information about the system at the
start of a time dependent study (see "study") ie . This is often
information which is provided through the type of study conducted. If
you mix 2 species (A and B) to react you often know how much A and B you
put into the system ie you know the initial concentrations for both. Or
if you heat up a pool before putting on the insulation cover, you know
the temperature before leaving it overnight.

## Interphase
The interphase is the region between two distinct phases (fx
liquid/solid, solid/gas etc.). It thereby describes the region where
properties transition from one bulk to the other fx how heat can be
transferred from a stove to the air. In computational modelling it can
often be an advantage to set an interphase as the boundary condition if
the problem allows for it like we did in project 2 with the
lagoon and surrounding air.

## Linkage equation
A linkage equation is an equation which connects the state variable (see
"state variable") with the governing equation (see "governing
equation"). If the governing equation doesn't give the information we
seek, we must link it with another equation to get the valuable
information.

## Lumped parameters
"Lumping parameters" is a method of model simplification (see "model
simplification") which consists of taking multiple contributions to a
physical phenomenon and placing them together in one expression. The
best example would be lumping a series of resistors into one resister by
summing them up [3]. It is however also possible to lump changing
parameters together IF the value of such parameters only change
minimally. In the coffee mug example from the lectures we lumped the
coffee liquid and coffee wall together assuming that the temperature
within the warm coffee was the same as the temperature of the outer wall
(red line on slide 3 = lumped, black line = not lumped) [4]. A problem
with lumping parameters is that this often introduces uniformity where
non-uniform behavior might exist (again see coffee mug example from the
lectures).

[3] <https://www.electronics-tutorials.ws/resistor/res_3.html>

[4]
<https://github.com/AU-BCE-EE/course-modelling-2025/blob/main/classes/03_02_sept_heat_transfer/solutions/coffee.pdf>

## Model simplification
Model simplification reduces the complexity of a model while retaining
essential behavior. In other words, model simplification is utilized to
decrease computation strain (ie decrease computation time/power). It
often involves assumptions, parameter reduction, or replacing
distributed models/parameters (see "distributed parameters") with lumped
(see "lumped parameters") ones to make analysis or computation more
efficient.

## Model validation
Model validation is when the computational model is compared to real
world scenarios and data. This means when we are validating the model we
are asking "are we building the *right* model" and is it representative
of the real world? In project 2 you compared the model to a set of data
given by Frederik and Sasha to validate your model.

## Model verification
Model verification is when a computational model is evaluated to see if
it has been implemented correctly according to the design. This means
that for verification we are asking "are we building the model *right*"?
Are the equations correct? Are they linked properly? Is the domain (see
"domain") properly described by the indexing (see "indexing")? In
project 2 you checked the units, ran edge cases, did troubleshooting
etc. in order to verify the model.

## Numeric solution
Numeric solutions are approximate solutions to a mathematical problem
using computational algorithms to estimate the exact solution within the
given domain (see "domain"). This also means that numeric solutions
aren't guaranteed to accurately describe the system outside the
specified domain. Numeric solutions are often utilized for complex
problems where analytical solutions aren't practically feasible. To
create a solution they utilize factors discretization such as the finite
difference method (see "finite difference method") and solver algorithms
such as the Euler, backwards Euler and Runge-Kutta methods.

## ODE
An ODE (ordinary differential equation) is a differential equation where
the dependent variable only changes with a single independent variable.
These are the type of differential equations which you have often seen
in examples fx $\frac{dy}{dx} = 2x + y$

## PDE
A PDE (partial differential equation) is a differential equation which
relates multiple variables to its partial derivatives. An example of a
partial differential equation is the heat conduction equation which
relates temperature to both time and space,
$\frac{dT}{dt}=\alpha \frac{\partial^2T}{\partial x^2}$. When working
with PDE's it is often preferable to convert the PDE to sets of ODEs
(see "ODE") by separation of variables if possible.

## Stability
Stability describes whether a numerical solution to a given problem
remains physically meaningful and bound as the computation progresses.
In other words, if a model is subjected to small changes or errors and
the algorithm starts spiraling out of control it is defined as "not
stable" producing unreliable results. An example of such "errors"/small
changes could be the rounding of numbers as the algorithm iteratively
solves the problem. If the model isn't stable, those differences will
constantly grow larger and larger until the error exceeds the specified
tolerance (see "tolerance") and the solution is discarded due to a lack
of convergence (see "convergence").

## State variable
The state variable is the variable of interest in the given study (see
"study"). If we look at heat transfer, we often what to express
"temperature" however we work with "heat transfer". In this case the
state variable is "temperature" while all other variables aren't.

## Steady state
Steady state describes a phenomenon in which the state variable (see
"state variable") (or any other variable) doesn't change with TIME. A
system can change over a domain ie you heat up a stick in one end and
cool at the other creating a temperature gradient through it but if the
temperature in a specific point doesn't change with time it is at steady
state.
