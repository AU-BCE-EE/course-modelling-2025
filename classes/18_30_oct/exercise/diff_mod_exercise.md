# 1D diffusion model verification and validation
Modelling 2025

In this exercise you will work with a 1D diffusion model.
You will get some practice in verification of conservation with 1D models and try model validation.
There are also two optional questions on some different ways to implement and verify (program) 1D models.

The conceptual model is quite simple.
We have a column with some solute (NaCl for example, which is what was used in the measurements) diffusing from one end to the other through water.
We can represent the conceptual model with text symbols:

```
       --------------------------
       |                        |
 c_l   |                        | c_r
 bc[0] |                        | bc[0] 
       |                        |
       --------------------------
       x -->
```

Both boundaries, at the left and right, have fixed concentrations.
And there is only one phase--an aqueous phase that is somehow stagnant (or assumed to be)!
This same model could also be used for a semi-infinite plane.

The model is implemented in the function `diff1D()` which is defined in the `diff_mod.py` module. 
Check the docstring and, if needed, `rates()` to see exactly what `diff1D()` returns before starting.

Note: The module now has several different versions of the model, each implemented as a separate function.
For the most part, the docstrings explain the differences.
You can use `diff1D()` and any variants of it that you make for this whole exercise.
It uses the node-based approach Frederik presented earlier in the semester.
The easiest version to understand is `diff1Db()` because it omits the cumulative mass transfer variables.
The `diff1Dc()` function and variants use a cell-based approach, which is easier for some people to understand.

1. Qualitatively describe what you expect this model predict, both after short and then long periods of time.

2. Given what you know about Fick's law of diffusion at steady-state in a plane wall, predict the steady-state flux of the solute without the model, and then compare your expected value to model predictions.

3. Can you use the output from the `diff1D()` to verify implementation of mass balance in the model?
Check the function docstring (look at the module file contents or run `help(diff1D)` in Python) to check function parameters and outputs.
This is meant to be a quick check, and not a detailed verification, but it is still good practice to keep a record of your function calls, output, and interpretation.
That could be done in many ways, including a Markdown document or `*.txt` file with code and output (manually pasted in), or an MS Word file, a Jupyter Notebook file, or a Quarto Markdown (`q.md`) file.

4. See the data file `col_salt.csv` for some (fabricated) measurements of the total salt (NaCl here) mass within a 0.1 m long column with a diameter of 0.02 m. 
Fixed salt concentrations at the boundaries were 36 kg/m3 at the left and zero at the right.
Use the measurements to validate the model graphically and with relevant model fit statistics.
The diffusivity of NaCl in water is known to be around 1.6E-9 m2/s.
What do you think about the accuracy of the model?
Hint: Be careful with units and variables. You have to convert model predictions to the variable that was measured.

Optional:
5. You may have noticed that the cumulative mass transfer at the left and right boundaries are both positive for flow to the right.
Create a new version of the `diff1D()` function and change this feature, so that both terms are positive for mass going into the column (model domain).
Make sure you give the new function a good name.
Save it in the same module as the original.
Now repeat your mass mass balance verification with this new function.

6. The code in the `rates()` function in `diff1Dc()` uses array indexing to efficiently calculate diffusion over spatial cells or layers.
Here is an example:
```{python}
        j = -D * (ca[1:] - ca[:-1]) / dxi
```
If we have say 5 cells or layers in the model, we could represent them like this:
```
   ca[0]    ca[1]     ca[2]     ca[3]     ca[4]  
```
And then this calculation
```{python}
ca[1:] - ca[:-1]
```
means this
```
   ca[1]    ca[2]     ca[3]     ca[4]  
 - ca[0]    ca[1]     ca[2]     ca[3]  
 -------------------------------------
```
and returns an array with those differences.
This is an efficient approach from a coding and evaluation (speed) perspective but it can be difficult to program or even understand!
The (new) `diff1D()` function uses a loop instead, which is easier for most people to understand (myself included)!
Create a new version of the `diff1D()` function that replaces the loop with clever indexing operations, or, instead, created a loop-based version of `diff1Dc()`.
Run the two and see that they gives the same results.

