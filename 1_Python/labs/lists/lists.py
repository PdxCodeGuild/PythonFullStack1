"""
# Given an input list, exclude an input integer and it's following element.
>>> exclude_em([56, 57, 58, 59, 60], 57)
[56, 59, 60]


>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34], 456)
[43, 67, 878, 5, 65, 34]


# Remove the first two element by default.
>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34])
[456, 23, 878, 5, 65, 34]


# Given two lists of ints, multiply numbers located at the same index
# in thier respective lists by each other. If the reusult is zero, append -1 instead.
>>> double([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0])
[86, 67, 456, 46, 1756, -1, -1, -1]


# Given two lists and an int, insert the elements of a list into the first list at the nth position
>>> punch_in([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0], 2)
[43, 67, 2, 1, 1, 2, 2, 0, 0, 0, 456, 23, 878, 5, 65, 34]
"""
