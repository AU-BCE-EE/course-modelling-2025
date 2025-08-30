# Cooling cup of coffee model

Develop a model for a cup of coffee cooling down toward ambient temperature.
Make any assumptions and simplifications that you think are helpful.

<img width="1024" height="732" alt="image" src="https://github.com/user-attachments/assets/94939751-e856-46eb-bc43-38e41acbcb39" />

<https://www.crazycoffeebean.com/how-to-cool-down-coffee-fast/>

If you need help getting started, think about these model formulation steps we went through in class on 28 August:

1. Initial concepts and assumptions (boundary, state variables, sketches)
2. Balance/conservation equations
3. Constitutive equations (transfer or rate equations)
4. Linking equations
5. Spatial or other simplifications
6. Initial or boundary conditions
7. Governing equation
8. Analytical or numerical solution

I know we did not spend time on all of those steps.
So here are some more specific suggestions:

* Develop an energy balance for the coffee, assuming that the cup itself does not bring any heat energy to the problem because it is initially at room temperature. This relates to step 2 above. Eliminate terms that are known or can be assumed to be zero or not relevant. What are you left with?
* We discussed only two constitutive equations for heat transfer, and then only briefly. Newton's law of cooling is a good fit for this problem (this relates to 3 above) and if you assume that internal resistance is negligible or, more accurately, can be *lumped* with external resistance to make an approximate model (related to 5 above), it is the only constitutive equation that you need for this problem. So write that down and make sure you understand the meaning of all the symbols.
* Think about how you can link the constitutive and balance equations. (This relates to 4 above.) To do that, you need some relationship between change in thermal energy and change in temperature.
* We did not really get to steps 7 or 8 above, and will discuss them next Tuesday 2 September. But see if you can start to put the pieces together to work toward a single equation that describes temperature over time. To related heat flux (Newton's law) to heat flow (energy balance) you will need the exposed surface area.
