"""

>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

>>> peaks(data)
[6, 14]

>>> valleys(data)
[9, 17]

>>> peaks_and_valleys(data)
[6, 9, 14, 17]

>>> points_of_interest = peaks_and_valleys(data)

>>> chop(data, points_of_interest)
[[1, 2, 3, 4, 5, 6, 7], [6, 5, 4], [5, 6, 7, 8, 9], [8, 7, 6], [7, 8, 9]]

"""
