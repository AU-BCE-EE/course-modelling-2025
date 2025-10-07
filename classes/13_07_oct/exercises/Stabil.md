

Exercises - Stability

1.  Sugar, S is converted to ethanol, E, in a batch reactor and the ODE
    systems is described like this:

    $dS/dt = -k_1 S$

    $dE/dt = 2k_1 S-k_2E$

    Determine whether the ODE system is stable or not by analyzing the
    eigenvalues and assume that the k values are positive.

2.  The diffusion equation is
    $\frac{\partial u}{\partial t} = D \, \frac{\partial^2 u}{\partial x^2}$

    Discretize the second order diffusion term with finite central
    difference. Is the system stable for the interior nodes? Does it
    matter how many interior nodes we have?

3.  The following ODE system is non-linear find the equilibrium points
    and determine their stability in each equilibrium point. Make some
    plots to confirm your findings.

    $dF/dt = F - 0.1FB$

    $dB/dt = 0.075FB - 1.5B$

4.  Imagine you have heat conduction in an iron rod of 1 meter

A\) Using the conductivity, heat capacity, and density of iron (find
online). What would you recommend the time step and space discretization
step to be if you were to solve the problem with explicit euler?

5.  Use the code for explicit euler by opening the file
    “explicit_euler_exercise.py” inside the demos folder.

A\) Read the code and try to understand what is going on, by adding you
own comments. What is different from our normal approach with solve_ivp?

B\) You are now going to solve the diffusion problem with this explicit
euler model. But running the code as it currently is gives an unstable
solution! Adjust time and space discretization to see what happens and
explain your observations.

C\) Could we do something smarter to solve this problem? What method
would you pick if you were to solve the problem with solve_ivp()?
