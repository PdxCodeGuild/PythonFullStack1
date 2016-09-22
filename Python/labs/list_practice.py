"""
# Given an input list, return it in reverse.
>>> backwards([56, 57, 58, 59, 60])
[60, 59, 58, 57, 56]


# Find the max number in a given list.  Then, change every element in the list containing the first number of the maximum to the maximum number.
>>> maximus([56, 57, 58, 59, 60])
[60, 57, 58, 59, 60]

>>> maximus([56, 67, 56, 59, 60])
[67, 67, 67, 59, 67]


# Given two lists, return True of the first two items are the equal.
>>> compare_first_element(['migratory', 'birds', 'fly', 'south'], ['migratory', 'monopoloy', 'mind'])
True

# Return True if the first letter of the second element in the list is the same. (case insensitive)
>>> compare_second_letter(['migratory', 'penguins', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
True

>>> compare_second_letter(['migratory', 'birds', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
False


# Given two lists, return one list, with all of the items of the first list, then the second
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'])
['mama', 'llama', 'baba', 'yaga']


# Use a default argument to allow the user to reverse the order!
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'], reverse=True)
['yaga', 'baba', 'llama', 'mama']


"""

def backwards(sequence):
    return sequence[::-1]


def maximus(sequence):
    biggest = max(sequence)
    first_digit = str(biggest)[0]
    counter = 0

    for item in list(sequence):
        if first_digit in str(item):
            sequence[counter] = biggest
            counter += 1
    return sequence

def compare_first_element(sequence, other_sequence):
    if sequence[0] == other_sequence[0]:
        return True
    else:
        return False

def compare_second_letter(sequence, other_sequence):
    if sequence[1][0] == other_sequence[1][0]:
        return True
    else:
        return False

def smoosh(sequence, other_sequence, reverse=False):
    if reverse == True:
        result = (sequence + other_sequence)[::-1]
    else:
        result = sequence + other_sequence
    return result
