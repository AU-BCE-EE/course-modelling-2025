# 1D model topics activity
Modelling 2025

# Activity description
There are five topics related to some important details of 1D transport modeling below. 
## Prepare
You and a partner will be assigned one of them by counting off in class.
Take about 10 - 20 minutes to come up with an answer/demonstration/explanation, using whatever approach you think is appropriate.
You might draw a few diagrams in a notebook, write (or copy/paste) some Python code into a script, or come up with a more clever and useful approach.
You can use any resource, including class material, internet searches (e.g., function help files), ChatGPT or other GAI, and instructors.

## Round 1
### Present
Once everyone is ready, half the groups will present the topic and your explanation to a different group of two students over four minutes, to help them understand the concept and, as appropriate, code.

### Learn
And half the groups will listen and learn for the first round.
Round 1 will take around 10 minutes.

## Rounds 2-4
For the next round, quickly find a new group, experts on a new topic, and repeat.
We will take about 40 minutes to go through all the rounds.

# 1.  
The diffusion functions in the `diff_mods` module all have code similar to this to repackage the output returned by `solve_ivp()`.

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
Could you replace the negative numbers with (different) positive numbers to extract the same results?
But would that work with a variable-sized array (with fewer or more nodes)?

# 2. 
Here is a representation of a numerical approach for solving a 1D diffusion problem.

<img width="1339" height="565" alt="image" src="https://github.com/user-attachments/assets/7120f7c4-14ce-4aa8-9741-5cb7eaea1f8b" />

Write and explain a mathematical equation (or Python pseudocode) for calculating diffusive flux at locations `a` and `b`.
Can you use this equation to come up with an equation for the derivative of solute concentration in cell 2?
Bonus: Is your result any different from the central difference method for calculating the time derivative of concentration?

# 3. 
The following code is from one of the 1D diffusion functions in the `diff_mods` module.

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
Bonus: Can you explain how it is possible to actually eliminate the loop and effectively carry out all iterations in one go using slicing?
You can find examples of this in the diffusion model module.

# 4. 
It is possible to predict whether a plane wall (1D rectangular system) is cooling or heating or at steady state just based on the shape of the temperature profile. 
(The same could be said for concentration change and a concentration profile, but let's use heat for a change.)
Take a look at the two profiles below, meant to be for a grid with six nodes.
Explain how you can tell whether the objects are heating or cooling by applying what you know about Fourier's law.
Hint: It might be helpful to think about heat flux at the boundaries between nodes.

<img width="1124" height="661" alt="image" src="https://github.com/user-attachments/assets/3407d5cb-d06c-46b7-9d9b-274b6cf0a62e" />

# 5. 
1D dynamic models typically return 2D arrays, where the rows are nodes or positions and the columns are times.
It can be tricky to work with these. 
Using some output from one of the diffusion models, explain how to tell which dimension is time and which is position, and demonstrate how to extract the following:
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

