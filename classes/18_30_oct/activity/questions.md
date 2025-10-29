# 1D model topics
Modelling 2025

1. The diffusion functions in the `diff_mods` module all have code similar to this to repackage the output returned by `solve_ivp()`.

```
out = {
    "t": res.t, 
    "dx": L/n, 
    "x": x, 
    "c": res.y[:-2, :], 
    "ml": res.y[-2, :], 
    "mr": res.y[-1, :]
}
```

Explain the weird stuff in square brackets for the last three elements.
What is it called?
It might be helpful to show some examples with Python or pencil and paper.
Explain if (and why) you need the first colon `:` on the `"c"` line.
Do you need the colons at the end, after the commas?
Do you need the comma?
Could you replace the negative numbers with positive numbers to extract the same results?
Would that work with a variable-sized array?

2. Here is a representation of a numerical approach for solving a 1D diffusion problem.


Write and explain a mathematical equation (or Python pseudocode) for calculating diffusive flux at locations `a` and `b`.
Can you use this equation to come up with an equation for the derivative of solute concentration in cell 2?
Bonus: Is your result any different from the central difference method for calculating the time derivative of concentration?



3. The following code is from one of the 1D diffusion functions in the `diff_mods` module.

```
for i in range(1, n):
    dcdt[i] = D * (ca[i + 1] - 2 * ca[i] + ca[i - 1]) / dx**2
```

Here, 
* `ca` is a 1D array with solute (perhaps NaCl) concentrations for multiple nodes or cells (kg/m3), with fixed concentrations in the first and last positions  (the boundary conditions),
* `dcdt` is an array of time derivatives of concentration for the same nodes (kg/m3-s),
* `D` is diffusivity (m2/s), and
* `dx` is the distance between nodes (m).

Explain or show how these two lines of code are used to calculate the time deriviative of solute concentration for all necessary nodes.
Use a drawing or Python code or whatever you find illuminating.

4. It is possible to predict whether a plane wall (1D rectangular system) is cooling or heating or at steady state just based on the shape of the temperature profile. 
(The same could be said for concentration change and a concentration profile, but let's use heat for a change.)
Take a look at the two profiles below, meant to be for a grid with six nodes.
Explain how you can tell whether the objects are heating or cooling by applying what you know about Fourier's law.
Hint: It might be helpful to think about heat flux at the boundaries between nodes.

5. 1D dynamic models typically return 2D arrays, where the rows are nodes or positions and the columns are times.
It can be tricky to work with these. 
Using some output from one of the diffusion models, demonstrate and explain how to extract the following:
* all nodes (positions) for a specific time,
* all times for a specific node,
* all nodes for the latest time (did you use a minus sign?), and
* anything else that you think is useful.

Sometimes you might need the sum of rows or columns.
See if you can find and explain how to use a NumPy function for calculating the sum of all rows while maintaining the different columns or vice versa.
For example, how can you go from this

```
0 1 2
0 3 4 
0 4 5
```

to this

```
0 8 11 
```

(column sums),
or this

```
3 7 9
```

(row sums)?




