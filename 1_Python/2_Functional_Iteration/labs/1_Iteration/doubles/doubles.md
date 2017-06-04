# Lab: List Doubles

###### Delivery Method: Doctests

--------------

##### Goal

Write a function to take a list, and return a new list with *each* element multiplied by n, excluding elements resulting in zero.

--------------------

##### Instructions

Write your function to accept two parameters: the input list and `n`.  Iterate over the list, and using a list building pattern multiplying each element by n.  If the product of an element and `n` is equal to 0, do not include it in the output list.


To execute the doctests, run `$ python -m doctest credit.py`

-------------------
#### Documentation

1. [Python Official: Operators](
https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions)

-----------------------

#### Advanced

- Write a solution that employs "python list comprehensions"

#### Super Advanced

- `from operator import mul`
- Use the `map()` builtin to map the `mul()` method over your list.

----------------------
#### Key Concepts

- `for` looping
- Operators
- Functions with multiple arguments
- Writing doctests
