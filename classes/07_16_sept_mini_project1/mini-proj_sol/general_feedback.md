# General mini-project feedback

## Overview 
Almost every group developed a logical and reasonable model, within the limits that come with trying to describe a complex system with a simple model and considering the challenge of presenting everything in no more than 5 pages!
And we did not give you much time either.
So, in general, nice work!
There are still things to improve for next time.
But first, the good things.
It was clear that you used the model formulation process we studied in class.
Sketches were quite good!
Most reports clearly stated that a lumped parameter approach was used.
Most of you recognized and explained that the models included other important simplifications.
Most of you used numerical solutions and did so correctly.
And almost all reports included plots that showed results clearly.
Because of the model simplifications and the difficulty in determining reasonable parameter values, the predicted temperature or ammonia loss were unlikely to be accurate from a quantiative perspective, but the qualitative responses almost always made sense as did the related explanations.

## Some tips
There were some common issues that showed up in multiple reports.
Everyone should read through the list of tips below and think about how you could have done things differently.

1. Recognize that there can be multiple routes for each term in the balance equation, e.g., heat loss from exposed water surface and through pool walls and floor. With a numerical approach, it is not difficult to handle these additional mathematical terms in the resulting governing equation. For our simple lumped-parameter models, it is even possible to come up with an analytical solution, although not quite as simply as in the examples we've discussed in class. The additional terms can make derivation of a steady-state solution a little tedious, but not really difficult.
1. Almost every submission could have benefited from more documentation, including 1) some kind of summary of the different Python scripts or functions, 2) a good docstring for each script and function, 3) comments throughout scripts, and 4) some information on units. 
1. Listing units in the report along with model equations and in Python scripts along with input data and model equation can help you avoid (or find) errors in the model itself or in its application.
1. Be efficient. Don't create a new model function for every application or demo. Instead you can write a general function that can be used for multiple applications. If a new scenario just differs though an input parameter (e.g., solar area), that just means calling the same function with a different input.
1. Almost everyone who used a numerical approach did so with `solve_ivp()` or `ode_int()` and a user-defined derivative (rates) function. That is OK. But it is even more efficient to write a function that has all your model code. Then in the application/demonstration/exploration you just need to call the model function. See the [coffee solution](https://github.com/AU-BCE-EE/course-modelling-2025/tree/main/classes/03_02_sept/solutions/coffee_function) for example. If you did use a function to implement your model, great. But then it is good practice to define it in one \*.py module and call it up in a separate \*.py script. No group did this, but it can make your code clearer, more modular, and easier to demostrate and use.
1. Try to follow the PEP 8 Style Guide for Python code (<https://peps.python.org/pep-0008/>). That means spaces after commas in most cases. The code can still run without following style rules, but like in written language,it Is dis*TRACT*ing-when wE don"t foLLOW        rules.
1. Your symbolic equations will be easier to understand if you use the same symbols that we try to use in class. See the list [here](https://github.com/AU-BCE-EE/course-modelling-2025/blob/main/docs/symbols.md). Otherwise, define your symbols. In at least two cases the governing equations ended up wrong apparently because of your own confusion caused by the use of unclear symbols!
1. Only a few reports described sources for parameter or variable values. That is not surprising considering the time you had to work on this project. But if possible, it would be good to be more clear about sources or to state that a value is a guess.
1. The word for a material that is intended to reduce heat transfer is "insulation" in English. Unfortunately "isolation" is another English word but with a different meaning (actually two different meanings). The Danish word for insulation is very similar to isolation and so I know this is confusing! And of course language is not my strength, so this is not criticism but a friendly tip.
1. Another language tip, but this one is technical. "Volatization" is the appropriate word when a chemical goes from a solution to a gas phase. Reserve "evaporation" for when a pure chemical goes from liquid to gas phase.
1. Most of you figued out ionization fraction calculations, which are basic and important. Here is a calculator for checking ammonia calculations: <https://github.com/AU-BCE-EE/course-modelling-2025/blob/main/docs/Free_NH3_calc.xlsx>.

## More feedback
The tips above do not cover all issues we saw; in a small number of cases, for example, the governing equations seemed quite wrong. 
So see the pdf and md files with feedback in Brightspace for comments that are specific to your report.
And please reach out by email if you would like to meet to discuss your report or code.
