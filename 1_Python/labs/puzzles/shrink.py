"""
Find the sum of each number in a string.
If the result is a more than one digit number,
continue to find resulting sums until the output is a single digit int.


For example: 1 + 2 + 3 + 5 = 11
Thats still more than one digit!
Repeat the same process with the result
11 is two digits so, 1 + 1 = 2

>>> shrink('1235')
2

>>> shrink('13')
4

>>> shrink('1123581321')
9

"""

# Write your code here.
