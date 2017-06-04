"""
>>> advise_player('A', 'K')
21 Blackjack!

>>> advise_player(10, 5)
15 Hit.

>>> advise_player('Q', 5)
15 Hit.

>>> advise_player('J', 'K')
20 Stay.

>>> advise_player(10, 5, 'J')
25 You lost.

>>> advise_player()
Traceback (most recent call last):
    ...
ValueError: Requires at least 2 arguments.
"""


# Write your code here...