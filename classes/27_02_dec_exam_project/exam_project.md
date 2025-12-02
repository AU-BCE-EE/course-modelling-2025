# Modelling 2025 exam project
Frederik R. Dalby and Sasha D. Hafner

Note: Help is offered from teachers and instructors only through December 4th. 

# Problem
You are an engineer working at Arla in the milk production unit. 
Milk needs to be treated at a ultra high temperature (UHT treatment) to kill bacteria, and this is done using a countercurrent pipe heat exchanger where the milk must be heated to 135 - 150 degree C for 5 seconds. 
After milk leaves the pipe heat exchanger it has to be cooled quickly to avoid a change in quality. 
See the diagram below.

```

insulated exterior ===========================
                   <-                        <-  hot steam
   thin pipe wall  ---------------------------
       cool milk ->                          ->  hot milk -> external cooling
                   ---------------------------
                   <-                        <-  hot steam
                   ===========================

```

You are on the team designing the heat exchanger. 
The stainless steel pipe for the heat exchanger comes only in a standard size with an inner diameter of 40 mm and a very thin wall. 
The incoming milk is 20 $^\circ\text{C}$ and you want to process 144 $\text{m}^3~\text{d}^{-1}$. 
For heating the milk you have steam that is 170 $^\circ\text{C}$. 
You can assume that the flow rate of steam is so high that the temperature is constant and uniform along the length of the heat exchanger. 

You are going to develop a model that can predict milk temperature along the length of the heat exchanger pipe, because this model will help answer the design question: how long should the pipe be for the milk to be above 135 $^\circ\text{C}$ for exactly 5 seconds?

You don't have any values for the heat transfer coefficient of the pipe heat exchanger, but you collected some data from a similar heat exchanger that was used for heating water instead of milk. 
In the measurement experiment 1 m of the interior pipe was filled with 20 $^\circ\text{C}$ water, water flow was stopped, and 120 $^\circ\text{C}$ steam flow was turned on.
The temperature was then measured in the water inside the pipe over time.    
Note that this batch operation is different from the way the heat exchanger will normally be operated, with milk constantly flowing through it, but the measurements still provide an estimate of the heat transfer coefficient and either a 1D or 0D model could be used for parameter estimation.

# Tasks
## 1. Model development
The first task is to develop the 1D model for predicting the milk temperature over the length of the heat exchanger. 
Include a sketch of the model and the system boundary.
Describe how you formulated the model and what assumptions you made, including information on the coordinate system, simplification of the governing equation, boundary conditions, and initial conditions.
For the Python implementation of your model, you should use a module-based approach (define a model function in a `*.py` module and then write the code for use of the model in separate `*.py` scripts).
Be sure to comment your code enough that someone could understand it without input from you--that information should be present in docstrings and single line comments.
Be sure to include units.

## 2. Model verification
Carry out some *limited* verification of your model by using some of the concepts taught in class.
For example, at least call the model a few times with some extreme values for important parameters or other inputs to show that it behaves as expected. 
Include documentation of your verification in an appendix, using whatever format or approach you think is appropriate.

## 3. Parameter estimation
Use the measurement data to carry out parameter estimation.
Be sure to check how well your model can reproduce the measured values using the resulting parameter estimate(s), e.g., by comparing measurements and model output graphically.
No additional validation is required beyond this.

## 4. Application
Use your model to predict the total length of the heat exchanger pipe needed to ensure that milk gets above 135 $^\circ\text{C}$ for 5 seconds.
Will the temperature exceed 150 $^\circ\text{C}$ and if so, what could be done to prevent it? 
Include plots to support your findings.

# Report
## Structure
You can use the following structure:
* Introduction (short, but do describe the system and problem),
* Model description (feel free to move details into an appendix)
* Model verification (show what you tested and found, documenting that the model behaves as you would expect, with code in an appendix),
* Parameter estimation (summarize what you have done and how well the model reproduces the measurements, with the code in an appendix)
* Model application (what length did you select? Show that it works)
* Conclusions (e.g., how could the work be improved?, or do you have some hypotheses or limitations that could be explored in the future?)
* Appendices, including Python code and any details on model verification, parameter estimation, formulation, or other things that didn't fit well in the main body of the report.

## Generative artifical intelligence (GAI)
You are not allowed to use AI for developing the model or writing the report, but can use it for factual information.

## Report length
The report should be no more than 10 pages, excluding appendices.

## Groups
You work on the project and report in groups of 3-5 people - remember to enroll yourself on brightspace as soon as possible so we can make the final exam plan!

## Deadline
Submit in Brightspace before December 23th 11.59 PM.

## Tips
### Heat transfer
Because the heat source is hot steam (water vapor) there will be some condensation as it heats the cool milk.
This process makes heat transfer very efficient, which is reflected in parameter values, but the process can be modelled just like the simpler case without a phase change.
In other words, you should not try to explicitly model any phase change!

### 1D models and heat transfer
You may find some hints from the following exercise solutions that we have worked with in the course: 
* Exercise 3 and 6: [classes/09_23_sept_1D_BC_types/solutions/BCs_ident.md](https://github.com/AU-BCE-EE/course-modelling-2025/tree/main/classes/09_23_sept_1D_BC_types/solutions) 
* Heat bed exercise: [classes/12_02_oct_2D_heat_bed/solutions/heatCond2D.md](https://github.com/AU-BCE-EE/course-modelling-2025/tree/main/classes/12_02_oct_2D_heat_bed/solutions)
* Exercise B and F: [classes/23_18_nov_mass_heat_reaction/solutions/mass_heat_reaction.md](https://github.com/AU-BCE-EE/course-modelling-2025/tree/main/classes/23_18_nov_mass_heat_reaction/solutions)

### Parameter estimation 
You can find information on parameter estimation in th class 25 demo (remember videos) and exercise solution: [classes/25_25_nov_par_est](https://github.com/AU-BCE-EE/course-modelling-2025/tree/main/classes/25_25_nov_par_est)


