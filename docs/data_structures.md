# Python tools for modeling I: data structures
Sasha D. Hafner

# 1. Overview

This document is part of a set meant to provide you (students) with a
review of basic Python tools that are important for modeling. Data
structures are the software objects that hold the numbers or other types
of data that are used in modeling. While it might be possible to do a
lot of modeling with scalars, e.g., a real number, called a *float* in
Python, putting multiple values in a single object makes writing and
using the model much simpler. You should always know the type of object
used in your code. Remember that the `type()` function can be used to
check within Python.

# 2. Scalars

The three essential types of scalars, or single-element objects, built
into Python are:

-   `int`: integers
-   `float`: real numbers or an approximation (float is for floating
    point)
-   `bool`: logical values (`True` and `False`, with bool for Boolean)

In many cases we’ll use these directly. In others they will be stored
within larger data structures.

``` python
x = 1
print(x)
print(type(x))
```

    1
    <class 'int'>

Integers will be converted to floats if used in arthmetic.

``` python
print(type(x / 2))
```

    <class 'float'>

``` python
pi = 3.14159
print(pi)
print(type(pi))
```

    3.14159
    <class 'float'>

``` python
b = True
print(b)
print(type(b))
```

    True
    <class 'bool'>

Boolean objects can also be converted to integers or floats. In that
case `True` is coerced or changed into the integer 1 and `False` to 0.

``` python
print(b + 1)
print(type(b + 1))
```

    2
    <class 'int'>

``` python
print(b + 0.5)
print(type(b + 0.5))
```

    1.5
    <class 'float'>

# 3. Lists

Lists are can contain multiple elements. There are multiple ways to
create them, but the simplest is with square brackets: `[` and `]`. For
example,

``` python
y = [1, 2.3, 4.5, 1.4]
print(y)
```

    [1, 2.3, 4.5, 1.4]

Lists can hold any scalar type (and can even take a mix of types, but
this can create confusion). The individual elements in a list can even
be other lists. This feature provides a way to simulate arrays using
lists. For example, you can effectively simulate a matrix like this

``` python
m = [[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
```

What is each element of `m`?

``` python
print(type(m[0]))
```

    <class 'list'>

A list. And we can think of each one as a row.

There are many built-in *methods* for lists. Remember that methods are
special functions that are always associated with a particular object.
They are called with a dot `.`. Below the `append()` method is used.

``` python
y = [1, 2.3, 4.5, 1.4]

y.append(10)

print(y)
```

    [1, 2.3, 4.5, 1.4, 10]

# 4. Tuples

Tuples look similar to arrays, but there are differences. The most
important is that tuples are *immutable*.

``` python
t = (1, 2, 3)
print(t)
```

    (1, 2, 3)

Being immutable means you cannot change the value of any elements. This
may be convenient sometimes, e.g., for model parameter storage.

``` python
t[1] = 2
```

    TypeError: 'tuple' object does not support item assignment
    [0;31m---------------------------------------------------------------------------[0m
    [0;31mTypeError[0m                                 Traceback (most recent call last)
    [0;32m/tmp/ipykernel_23290/2723529632.py[0m in [0;36m<module>[0;34m[0m
    [0;32m----> 1[0;31m [0mt[0m[0;34m[[0m[0;36m1[0m[0;34m][0m [0;34m=[0m [0;36m2[0m[0;34m[0m[0;34m[0m[0m
    [0m
    [0;31mTypeError[0m: 'tuple' object does not support item assignment

Another difference between the two data structures is that there are
fewer methods available for tuples.

# 5. Arrays

Proper arrays are typically better than lists (and certainly tuples) for
working with array-like data when developing models in Python. There are
many different ways to create NumPy arrays. For example, we can use
lists. Here is a one-dimensional (1D) array, or a vector, for example.

``` python
import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
print(type(a))
```

    [1 2 3 4]
    <class 'numpy.ndarray'>

Lists can even be used to create arrays with more dimensions.

``` python
a2 = np.array([[1, 2], 
               [3, 4]])

print(a2)
               
a3 = np.array([[[1, 2], [3, 4]], 
               [[5, 6], [7, 8]]])

print(a3)
```

    [[1 2]
     [3 4]]
    [[[1 2]
      [3 4]]

     [[5 6]
      [7 8]]]

You can check the dimensions with the `shape` attribute.

``` python
print(a.shape)
print(a2.shape)
print(a3.shape)
```

    (4,)
    (2, 2)
    (2, 2, 2)

Or, for just the number of dimensions,

``` python
print(len(a3.shape))
```

    3

There are other convenient ways to make arrays. Here are a few.

``` python
z1 = np.zeros(10)
print(z1)

z2 = np.zeros((3, 3))
print(z2)

z3 = np.zeros((2, 2, 2))
print(z3)
```

    [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
    [[0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]]
    [[[0. 0.]
      [0. 0.]]

     [[0. 0.]
      [0. 0.]]]

There is also a `ones()` function in NumPy.

# 6. DataFrames

The pandas package provides a data structure suitable for *tabular* data
called a data frame, or, in pandas parlance, a *DataFrame* (note the
capitalization, but “pandas” itself is not capitalized). Unlike an
array, a data frame can contain data of different types. See the `mm`
object below for an example.

``` python
import pandas as pd
mm = pd.read_csv('../data/mol_mass.csv', skiprows = 0)
```

``` python
print(mm)
```

         form  mol_mass
    0    CH4O    32.042
    1    C7H8    92.134
    2    C5H8    68.114
    3   C7H6O   106.118
    4   C3H6O    58.078
    5   C2H4O    44.052
    6  C2H4O2    60.052
    7   C4H8O    72.104
    8  C10H16   136.228

These molar mass have data of type string in the first column, and
floating point in the second. The `mm` DataFrame has *column names*,
which can be used to refer to individual columns.

The pandas package provides tools for processing complete DataFrames or
individual columns. And it contains features to maintain the connections
between the columns, so, for example, the formula in the second row is
always associated with the correct molar mass.
