# General steps in model formulation

1. Initial concepts and assumptions (boundary, state variables, sketches)
2. Balance/conservation equations
3. Constitutive equations (transfer or rate equations)
4. Linking equations
5. Spatial or other simplifications
6. Initial or boundary conditions
7. Governing equation
8. Analytical or numerical solution

# Algorithm for 1D models and getting to python

1. Select PDE coordinate system
2. Eliminate uneccesary terms (e.g. dimensions) to arrive at governing equation
3. Reformulate to discretized form (method of lines)
4. Figure out what BC's and IC's you have
5. Implement in python by handling interior nodes and BC nodes separately

