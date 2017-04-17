# Lab: Peaks and Valleys

###### Delivery Method: Doctests

--------------

##### Goal

Write three functions to satisfy the doctest's expected output.


--------------------

##### Instructions

Define the following functions:

1. `peaks` - Returns the indices of peaks. A peak has a lower number on both the left and the right.

1. `valleys` - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

1. `peaks_and_valleys` - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

1. `chop` - uses the aboce functions to generate a data structure: a list of lists, each list representing a single "slope" or area from peak to valley (terminally inclusive).

Here is a reference of the test data:

| Data    |  1 | 2 | 3 | 4 | 5 | 6 | 7 | 6 | 5 | 4 | 5 | 6 | 7 | 8 | 9 | 8 | 7 | 6 | 7 | 8 | 9 |
|---------|----|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Index   |  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20|
| POI     |    |   |   |   |   |   | P |   |   | V |   |   |   |   | P |   |   | V |   |   |   |
| Slope # |  1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 |
| Slope 1 |  1 | 2 | 3 | 4 | 5 | 6 | 7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Slope 2 |    |   |   |   |   |   |   | 6 | 5 | 4 |   |   |   |   |   |   |   |   |   |   |   |
| Slope 3 |    |   |   |   |   |   |   |   |   |   | 5 | 6 | 7 | 8 | 9 |   |   |   |   |   |   |
| Slope 4 |    |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 8 | 7 | 6 |   |   |   |
| Slope 5 |    |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 7 | 8 | 9 |

-------------------

#### Documentation

1. [Python Official: List Methods](https://docs.python.org/3/tutorial/datastructures.html)

1. [Python Official: For Statements operations](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

----------------------

#### Key Concepts

- Multi Functional Modules
- Function Definition
- Idiomatic python: D.R.Y.
- `for` looping
- Getting the index in scope inside a loop
- Look arounds
- Edge Detection
- List slicing
