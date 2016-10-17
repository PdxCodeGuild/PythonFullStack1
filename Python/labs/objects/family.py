"""
Given the following doctest, write a function named 'build_tree' that returns
an instance of the Person class representing the eldest member of the family.

Test the Person class.
>>> kieran = Person('Kieran')
>>> kieran.name
'Kieran'
>>> kieran.children

Set Up Some Variables for the Doctest... Each tuple is (child, parent).
>>> family = [('Terri', 'MoMo'), ('Bob', 'MoMo'), ('Kieran', 'Terri'), ('Lynn', 'Terri')]
>>> eldest_name = 'MoMo'

Build the family tree.
>>> momo = build_tree(eldest_name, family)
>>> momo.children
['Terri', 'Bob']
>>> momo.children[0].children
['Kieran', 'Lynn']
>>> momo.children[1].children

"""

class Person:
    pass

    def __init__(self, name):
        pass


def build_tree(family, eldest_name):
    pass
