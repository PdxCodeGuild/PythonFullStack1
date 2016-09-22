"""
# Return the count of a letter in a string.
>>> count_letter('i', 'Antidisestablishmentterianism')
5

>>> count_letter('p', 'Pneumonoultramicroscopicsilicovolcanoconiosis')
2

>>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
the latest letter is v.


>>> lower_case("SUPER!")
'super!'

>>> lower_case("        NANNANANANA BATMAN        ")
'nannananana batman'

# return the number of letter occourances in a string.
>>> locate('l', 'hello')
2
"""

def count_letter(letter, word):
    letter_count = word.lower().count(letter)
    return letter_count

def latest_letter(word):
    latest = 'a'
    for letter in word:
        if (letter > latest):
            latest = letter
    return "the latest letter is {}.".format(latest)

def lower_case(word):
    word = word.lower().strip()
    return word
