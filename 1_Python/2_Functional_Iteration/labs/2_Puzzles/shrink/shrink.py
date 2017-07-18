"""

>>> shrink('1235')
2

>>> shrink('13')
4

>>> shrink('1123581321')
9

"""

def shrink(numbers):
    numbers_sum = str(sum(int(n) for n in numbers))
    if len(numbers_sum) > 1:
        return shrink(numbers_sum)
    else:
        return int(numbers_sum)
