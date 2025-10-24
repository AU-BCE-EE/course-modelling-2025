# 1D diffusion model verfication
Modelling 2025

In this exercise you will work with a 1D diffusion model.
You will get some practice in verification of conservation with 1D models and also ways to implement (program) 1D models.
The model implemented in the function `diff1D()` which is defined in the `diff_mod.py` module. 
Check the docstring and, if needed, `rates()` to see exactly what `diff1D()` returns before starting.

1. Can you use the output from the `diff1D()` to verify implementation of mass balance in the model?
Check the function docstring (look at the module file contents or run `help(diff1D)` in Python) to check function parameters and outputs.
Keep a record of your function calls, output, and interpretation.
This could be done in many ways, including a Markdown document or `*.txt` file with code and output (manually pasted in), or an MS Word file, a Jupyter Notebook file, or a compiled `q.md` file.

2. You may have noticed that the cumulative mass transfer at the left and right boundaries are both positive for flow to the right.
Create a new version of the `diff1D()` function and change this feature, so that both terms are positive for mass going into the column (model domain).
Make sure you give the new function a good name.
Save it in the same module as the original.
Now repeat your mass mass balance verification with this new function.

3. The code in the `rates()` function in `diff1D()` uses array indexing to efficiently calculate diffusion over spatial cells or layers.
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
This is a handy approach but can be difficult to program or even understand!
Create a new (now third) version of the `diff1D()` function that replaces the clever indexing operations with `for` loops as in some of the 1D code you have seen before in this course.
Run it and show that it gives the same results as the original function.

