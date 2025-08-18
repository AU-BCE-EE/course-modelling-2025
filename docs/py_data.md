# Python data structures for modeling
Sasha D. Hafner

# 1. Overview

This document provides a review of basic Python structures that are
important for modeling. Data structures are the software objects that
hold the numbers or other types of data that are used in modeling. While
it might be possible to do a lot of modeling with scalars, e.g., a real
number, called a *float* in Python, putting multiple values in a single
object makes writing and using the model much simpler. You should always
know the type of object used in your code. Remember that the `type()`
function can be used to check within Python. The multi-element data
structures covered in this document are summarized in the table below.

| Structure | Mutable? | Example usage | More details |
|----|----|----|----|
| list | Yes | Input data, sequences | Many methods, append(), pop(), etc. |
| tuple | No | Fixed sequences, parameters | Fewer methods |
| array | Yes | Efficient numerical computation | Supports element-wise (vectorized) math |
| dictionary | Yes | Output with named elements | Get element values with keys |

# 2. Scalars

The three essential types of scalars, or single-element objects, built
into Python are:

- `int`: integers
- `float`: real numbers or an approximation (float is for floating
  point)
- `bool`: logical values (`True` and `False`, with bool for Boolean)

In some cases we’ll use these directly. In others they will be stored
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
case `True` is coerced (changed) into the integer `1` and `False` to
`0`.

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

Lastly, strings are used for storing text data in Python. Double or
single quotes can be used, but double are more common.

``` python
s = "Time (h)"
print(s)
```

    Time (h)

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

A list. And we can think of each one as a row. But the array
functionality from the NumPy package is more efficient and we’ll use
that approach in this course.

There are many built-in *methods* for lists. Remember that methods are
special functions that are always associated with a particular object.
They are called with a dot `.`. Below the `append()` method is used.

``` python
y = [1, 2.3, 4.5, 1.4]

y.append(10)

print(y)
```

    [1, 2.3, 4.5, 1.4, 10]

Lists support indexing or slicing, which is a powerful tool for data
manipulation that will be used extensively in our course. For example,
we can extract the first element like this.

``` python
y[0]
```

    1

Second element.

``` python
y[1]
```

    2.3

For reference, here is the entire list again.

``` python
y
```

    [1, 2.3, 4.5, 1.4, 10]

Here is syntax for the last element.

``` python
y[-1]
```

    10

Or take what is called a “slice” using a colon operator.

``` python
y[1:3]
```

    [2.3, 4.5]

This gives elements in position 1 and 2, which is confusing for many.
Note that the syntax is the same as the `range()` function.

Omitting one of the indices returns everything *from* or *up to* the
other index.

``` python
y[1:]
y[:1]
```

    [1]

``` python
y[2:]
y[:2]
```

    [1, 2.3]

Indexing can be used for assignment as well.

``` python
y
y[1] = 0
y
```

    [1, 0, 4.5, 1.4, 10]

But to use the slice notation to assign to more than one position, we
need a list (or other “iterable”) on the right, like this.

``` python
y
y[1:3] = [100, -100]
y
```

    [1, 100, -100, 1.4, 10]

# 4. Tuples

Tuples look similar to lists, but there are differences. The most
important is that tuples are *immutable*.

``` python
t = (1, 2, 3)
print(t)
```

    (1, 2, 3)

Indexing is similar to lists.

``` python
t[2]
```

    3

Being immutable means you cannot change the value of any elements. This
may be convenient sometimes, e.g., for model parameter storage.

``` python
t[1] = 2
```

    TypeError: 'tuple' object does not support item assignment
    [0;31m---------------------------------------------------------------------------[0m
    [0;31mTypeError[0m                                 Traceback (most recent call last)
    Cell [0;32mIn[23], line 1[0m
    [0;32m----> 1[0m [43mt[49m[43m[[49m[38;5;241;43m1[39;49m[43m][49m [38;5;241m=[39m [38;5;241m2[39m

    [0;31mTypeError[0m: 'tuple' object does not support item assignment

Another difference between the two data structures is that there are
fewer methods available for tuples.

# 5. Arrays

Proper NumPy arrays are typically better than lists (and certainly
tuples) for working with array-like data when developing models in
Python. There are many different ways to create NumPy arrays. For
example, we can use lists. Here is a one-dimensional (1D) array, or a
vector, for example.

``` python
import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
print(type(a))
```

    [1 2 3 4]
    <class 'numpy.ndarray'>

Lists can even be used to create arrays with more dimensions. (Notice
the similarity here between the `np.array()` argument and the use of
lists as arrays shown above.)

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

Or, for just the number of dimensions:

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

There is an analogous `ones()` function in NumPy as well.

Arrays support indexing (extraction and assignment) as well.

``` python
a2 = np.array([[1, 2], 
               [3, 4]])

a2
```

    array([[1, 2],
           [3, 4]])

Separate the indices for different dimensions with commas.

``` python
a2[1, 1]
```

    4

Assingment works too.

``` python
a2[1, 1] = 0
a2
```

    array([[1, 2],
           [3, 0]])

And so does slicing, for both extraction and assignment.

``` python
a2[0:2, 1] 
```

    array([2, 0])

Omit the indices but leave the colon to get all elements in a particular
dimension.

``` python
a2[:, 1] 
```

    array([2, 0])

``` python
a2[0, :] = [-10, -10] 
a2
```

    array([[-10, -10],
           [  3,   0]])

Arrays also support vectorized operations, which is very useful. So, for
example, to multiple every element in `a2` by 10.

``` python
a20 = 10 * a2
a20
```

    array([[-100, -100],
           [  30,    0]])

This might seem trivial, but it has not been the norm in programming
languages, and does not work in lists, for example.

``` python
3 * [1, 2, 3]
```

    [1, 2, 3, 1, 2, 3, 1, 2, 3]

Instead, Python does what is called *sequence repetition*.

# 6. Dictionaries

Dictionaries are handy when data elements need some kind of label or
name to go along with them, such as with model output.

``` python
out = {
  "model": "Diff1D",
  "iterations": 3,
  "fit": 0.9
}

out
```

    {'model': 'Diff1D', 'iterations': 3, 'fit': 0.9}

Of course they are more useful when the values are linked to symbolic
variables! The keys (names) are used to extact or set elements.

``` python
out['fit']
```

    0.9

There is also a `get()` method.

``` python
out.get('fit')
```

    0.9

And the `keys()` method is handy for larger dictionaries.

``` python
out.keys()
```

    dict_keys(['model', 'iterations', 'fit'])

# 7. DataFrames

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
individual columns (Series in pandas terminology). And it contains
features to maintain the connections between the columns, so, for
example, the formula in the second row is always associated with the
correct molar mass.

We may use DataFrames for importing and exporting data, and possibly for
some data processing. But in most cases, the other data types are
simpler for our work.

What if we want to work with a column of data? We can use either a dot
`.` or the general Python and NumPy indexing operator square brackets
`[ ]`, as shown above.

``` python
print(mm.mol_mass)
```

    0     32.042
    1     92.134
    2     68.114
    3    106.118
    4     58.078
    5     44.052
    6     60.052
    7     72.104
    8    136.228
    Name: mol_mass, dtype: float64

``` python
mm_vals = mm.mol_mass
print(mm_vals)
```

    0     32.042
    1     92.134
    2     68.114
    3    106.118
    4     58.078
    5     44.052
    6     60.052
    7     72.104
    8    136.228
    Name: mol_mass, dtype: float64

``` python
mm_vals = mm['mol_mass']
print(mm_vals)
```

    0     32.042
    1     92.134
    2     68.114
    3    106.118
    4     58.078
    5     44.052
    6     60.052
    7     72.104
    8    136.228
    Name: mol_mass, dtype: float64

We can then work with the “extracted” values. But be careful! The class
is Series, a special pandas class, not a simple array. Second, the
`mm_vals` object is *still* part of the larger DataFrame.

Typically, a better option is to extract the values with the `array`
attribute.

``` python
mm_vals2 = mm.mol_mass.array
print(mm_vals2)
```

    <NumpyExtensionArray>
    [32.042, 92.134, 68.114, 106.118, 58.078, 44.052, 60.052, 72.104, 136.228]
    Length: 9, dtype: float64

Now we can use these as any other array.

``` python
print(min(mm_vals2))
print(mm_vals2.mean())
```

    32.042
    74.32466666666667

(Which `mean()` method do you think are we using in the second line
above? Remember that it depends on the class of the object.)

Alternatively, the `to_numpy()` method may have some advantages.

``` python
mm_vals3 = mm.mol_mass.to_numpy()
print(mm_vals3)
```

    [ 32.042  92.134  68.114 106.118  58.078  44.052  60.052  72.104 136.228]

Originally the pandas documentation recommended using the `.values`
attribute to get the underlying values, but does no longer (see here for
some explanation:
<https://pandas.pydata.org/docs/user_guide/basics.html>). But you will
still see `.values` in answers and more online.
