"""
>>> snake = Animal()

>>> snake.is_animal
True

>>> snake.is_vegetable
False

>>> snake.is_mineral
False

>>> snake.number_of_legs
0

>>> snake.what_i_say is None
True

>>> snake.speak()
Sorry, I don’t speak!

>>> llama = Animal(legs=3, say='shazbat')

>>> llama.is_animal
True

>>> llama.is_vegetable
False

>>> llama.is_mineral
False

>>> llama.number_of_legs
3

>>> llama.what_i_say is None
False

>>> llama.speak()
shazbat
"""
