# Mini-project 2: 1D reaction-transport model

Develop a model for oxygen transport and organic matter (OM) consumption by bacteria in an open-top wastewater "polishing" lagoon without inflow or outflow. 
Assume that the wastewater is stagnant (so transport is by diffusion only) and contains OM that is consumed by aerobic bacteria only. 
In the model you need to include at least dissolved oxygen and OM as state variables and you can assume that OM degradation is a second-order reaction. 
You can also assume that it takes 1 gram of oxygen to degrade 1 gram of OM. 
(In fact this is usually done in the wastewater treatment field because organic matter is expressed in "oxygen demand" units.)

## Tasks
## 1. Model development
The first task is to develop the 1D model of the wastewater tank with oxygen and OM as state variables. 
Include a sketch of the model and the system boundary.
Describe how you formulated the model and what assumptions you made, including information on the coordinate system, simplification of the governing equations, boundary conditions, and initial conditions.   
For your Python code, you should use a module-based approach for your model (define a model function in a `*.py` module and then write the code for verification, validation, and application in separate `*.py` scripts).
Be sure to comment your code enough that someone could understand it without input from you!
That information should be present in docstrings and single line comments.

## 2. Model verification
Carry out some limited verification of your model by using some of the concepts taught in class. 
Make sure that one of your verification checks includes mass conservation.  
Include documentation of your verification in an appendix, using whatever format or approach you think is appropriate.

## 3. Model validation
An engineer at the wastewater plant measured the concentration of dissolved oxygen near the bottom of a 10 cm deep lagoon over a couple months, starting right after filling.  
The measurement data are in the `meas_O2.csv` file. 
The filling process effectively aerated the wastewater at the start, but as you can see in the measurements, dissolved oxygen concentration declined over the following days.
The initial OM concentration was 0.02 kg/m3 (20 mg/L).
Carry out graphical and quantitative model validation using these measurements.

## 4. Model application
Use your model to predict at least one of the following:
* how long time it takes to degrade most (at least 90%) of the initial OM in an 10 cm deep lagoon, 
* the minimum dissolved oxygen concentration in the lagoon with 10 cm wastewater and time it occurs after loading a new batch of wastewater, 
* the effect of increasing dissolved oxygen diffusivity (what could that represent?), or
* the effect of increased or decreased substrate degradation rate.

Include plots to support your findings.

## Report
### Structure
You can use the following structure:
* Introduction (short, but do describe the system and problem),
* Model description (feel free to move details into an appendix)
* Model verification (it is OK to just summarize verification here and put details in an appendix, if you prefer)
* Model validation (be sure to include graphical and quantitative validation!)
* Model application
* Conclusions (e.g., what do you think of your model?, how could the work be improved?, did you have any unresolved problems?, what else would you like to know about the physical/biological system?, did you get any insights into the system or how to could be better managed based on your model?, or do you have some hypotheses that could be explored in the future?)
* Appendices, including Python code and any details on model verification, formulation, or other things that didn't fit well in the main body of the report.

### Generative artifical intelligence (GAI)
You are not allowed to use AI for developing the model or writing the report, but can use it for factual information.

### Report length
The report should be no more than 10 pages, including any appendices (fewer preferred--if you can do it in 5 pages, we will be happy and impressed).

### Groups
You work on the project and report in groups of 3-5 people.

### Deadline
Submit in Brightspace before 23:59 on friday the 14th of November. 

## Tips
* See the [document on parameter values](https://github.com/AU-BCE-EE/course-modelling-2025/blob/main/docs/parameter_values.md) for some helpful information.
* The concentration of $\text{O}_2$ in pure water in equilibrium with the atmosphere is around 10 mg/L. You can use this value without explicitly simulating inter-phase mass transfer if you assume all the resistance to wastewater aeration in this system is present in the water, which is reasonable. 
* The diffusivity of dissolved oxygen in water is around $2.1 \cdot 10^{-9}$ $\text{m}^2 ~ \text{s}^{-1}$. For OM you can assume that it mainly consist of very small molecules like glucose. 
* Second-order rate constants can be estimated by fixing one reactant concentration (say, $\text{O}_2$ here) and then solving for the $k$ value that matches an observed reaction rate. 
For example, if you know that organic matter is degraded at a first-order rate of around 10% per day when dissolved $\text{O}_2$ is 0.01 kg/m3, you need a second-order rate constant of 10 m3/kg-d (this is from 0.1 1/d = k m3/kg-d * 0.01 kg/m3 -> k = 0.1 / 0.01 = 10 m3/kg-d), which is about 1.2E-4 m3/kg-s. This is actually a reasonable estimate for this model. 
* Remember that you have examples of 1D models to help (see slides, demos, and exercise solutions from relevant classes).
* Remember to include `reload()` in your testing script to make sure you are working with the updated version of your model function after you edit it.

## Encouragement
If you are struggling with 1D models and do not even know where to start, that is OK! 
This mini-project is a chance to learn.
You have five of us available to help you (four in-person and one online). 
Please ask for help if you are stuck or even if you just want some feedback on your work so far. 
