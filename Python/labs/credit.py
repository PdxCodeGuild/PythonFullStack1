"""
1. Slice off the last digit.
That is the **check digit**.
1. Reverse the digits.
1. Double every other element in the reversed list.
1. Subtract nine from numbers over nine.
1. Sum all values.
1. Take the second digit of that sum.
1. If that matches the check digit, the whole card number is valid.

For example, the worked out steps would be:

1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
1. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
1. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
1. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
1. 85
1. 5
1. Valid!


>>> validate([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])
Valid!

>>> validate([6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4])
Invalid!


"""
def validate(credit_number):
    check_digit = credit_number.pop()
    reversed_list = credit_number[::-1]














    for index, item in enumerate(reversed_list):
        if index % 2 == 0:
            reversed_list[index] = item * 2
    subtracted = [i - 9 for i in reversed_list if i > 9]
    result = str(sum(subtracted))[1]

    if result == '5':
        print("Valid!")

    else:
        print("Invalid!")
