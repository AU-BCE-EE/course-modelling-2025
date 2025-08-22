# Finite difference formulas

## approximation of the first derivative: $\frac{dc}{dx}$

### first order accuracy:

forward difference formula: $\frac{c[i+1] - c[i]}{\Delta x}$

backward difference formula: $\frac{c[i] - c[i-1]}{\Delta x}$

### second order accuracy:

forward difference formula: $\frac{-3c[i] + 4c[i+1] - c[i+2]}{2\Delta x}$

backward difference formula: $\frac{3c[i] - 4c[i-1] + c[i-2]}{2\Delta x}$

central difference formula: $\frac{c[i+1] - c[i-1]}{2\Delta x}$

## approximation of the second derivative: $\frac{d^2c}{dx^2}$

### first order accuracy:

forward difference formula: $\frac{c[i] - 2c[i+1] + c[i+2]}{\Delta x^2}$

backward difference formula: $\frac{c[i] - 2c[i-1] + c[i-2]}{\Delta x^2}$

### second order accuracy:

forward difference formula: $\frac{-c[i] + 4c[i+1] - 5c[i+2] + 2c[i+3]}{\Delta x^2}$

backward difference formula: $\frac{-c[i] + 4c[i-1] - 5c[i-2] + 2c[i-3]}{\Delta x^2}$

central difference formula: $\frac{c[i+1] - 2c[i] + c[i-1]}{\Delta x^2}$
