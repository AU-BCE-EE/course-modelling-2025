# Description of mini-project 2 solution files

* `model_formulation.pdf`: Derivation of the mathematical model (and a bit on Python implementation)
* `O2dc_mod.py`: Module with a single function `O2dc()`, which is the implementation of the model in Python (Python module)
* `demo.py`: A simple demo of the model function (Python script)
* `mass_bal.py`: Mass balance verification of the model function (Python script)
* `validation.py`: Validation of the model with measurements (Python script)
* `grid_res.py`: Evaluation of effect of model grid resolution (Python script)
* `application.py`: Application of the model as requested in project description


Note that some of the scripts produce plots, which are saved directly in a `plots` subdirectory.
The `validation.py` script saves merged measurements and model output along with model fit statistics in the `output` subdirectory.
You can download them from the GitHub page or recreate them by running the scripts (recommended).

The scripts are meant to be run interactively, although most could be run in batch mode.
The mass balance verification results are simply printed in the console, so running in batch mode will not show results.
The scripts could be extended with a `print()` call though. 
And results could be combined and exported like in `validation.py`.

Note that there are many correct variations that you could have used to implement the model!
You can see some possibilities in the `alternative` subdirectory that has some alternatives that you can check out if you are interested or if you used a different approach to implement your model than what you see in the `O2dc_mods.py` module.
Note that these versions are not as clearly commented as the original.
And one is not even complete.
Here is how they differ:

* `O2dc_mods_up.py` is like the original but the relationship between array and conceptual model direction is reversed, do position `[0]` is at the *bottom* of the lagoon.
* `O2dc_mods_1eq.py` takes advantage of the use of ghost points and the central difference method to calculate concentration time derivatives using the same code for interior and boundary nodes. The disadvantages are that the state variable arrays have to be extended first in `rates()` and that the `i - 1` etc. indices used are shifted by one place because of the added ghost points.
* `O2dc_mods_cell.py` uses a cell-based approach instead of the normal node-based approach. It separately calculates flux between all cells and then uses that for calculating the conconcentration derivatives (resulting in the central difference formula intuitively), and uses `dx/2` at the boundaries. The disadvantages is the need for a `dx` array instead of a scalar. 
* `O2dc_mods_imp.py` is node-based but uses an `N` input parameter for number of nodes instead of `dx`. This way it is not essential that `dx` is a factor of the total depth. Output times are specified directly with `t_eval`, making model validation easier. This version is not complete--take the code as a demonstration.

Lastly, `model_formulation_cell.pdf` has model formulation for an intuitive cell-based approach based on the 8 steps we covered at the beginning of class (i.e., not skipping to the GE from the book). 

