"""
>>> phonebook = {'kieran': {'name': 'Kieran R. Prasch',
                            'number':8456331959,
                            'phrase': 'Good code is not written, it's re-written.'},
                'guildbot': {'name': 'Lambda C. Doe',
                             'number':8454185633,
                             'phrase': 'Do or do not do, there is no try.'}}


>>> lookup('kieran')
Kieran R. Prasch - #845-633-1959
Good code is not written, it's re-written.

>>> lookup('guildbot')
Lambda C. Doe - #845-418-5633
Do or do not do, there is no try.

>>> update(number=5555555555, name='Fake McFakeson', phrase='He's a real nowhere man, sitting in his nowhere land, making all his nowhere plans for nobody.')
Updated Fake McFakeson with #555-555-5555.

>>> update

>>> remove()

>>> remove('Chuck Norris')
No entries found.

"""
