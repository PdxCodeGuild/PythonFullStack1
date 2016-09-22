"""
    >>> no_args_animal = Animal()
    >>> no_args_animal.is_animal
    True
    >>> no_args_animal.is_vegetable
    False
    >>> no_args_animal.is_mineral
    False
    >>> no_args_animal.number_of_legs
    0
    >>> no_args_animal.what_i_say is None
    True
    >>> no_args_animal.speak()
    Sorry, I don’t speak!

    >>> animal_with_args = Animal(number_of_legs=3, what_i_say='shazbat')
    >>> animal_with_args.is_animal
    True
    >>> animal_with_args.is_vegetable
    False
    >>> animal_with_args.is_mineral
    False
    >>> animal_with_args.number_of_legs
    3
    >>> animal_with_args.what_i_say is None
    False
    >>> animal_with_args.speak()
    shazbat

    """,
    'Dog': """

    >>> no_args_dog = Dog()
    >>> no_args_dog.is_animal
    True
    >>> no_args_dog.number_of_legs
    4
    >>> no_args_dog.speak()
    ruff
    >>> no_args_dog.kind
    'canine'
    >>> no_args_dog.wag()
    /wags tail

    """,
    'Pet': """

    >>> no_args_pet = Pet()
    >>> no_args_pet.name is None
    True

    >>> pet_with_arg = Pet(name='Puddles')
    >>> pet_with_arg.name is None
    False

    """,
    'PetDog': """

    >>> no_args_pet_dog = PetDog()
    >>> no_args_pet_dog.is_animal
    True
    >>> no_args_pet_dog.number_of_legs
    4
    >>> no_args_pet_dog.speak()
    ruff
    >>> no_args_pet_dog.kind
    'canine'
    >>> no_args_pet_dog.wag()
    /wags tail
    >>> no_args_pet_dog.name is None
    True

    >>> pet_dog_with_arg = PetDog(name='Fido')
    >>> pet_dog_with_arg.is_animal
    True
    >>> pet_dog_with_arg.number_of_legs
    4
    >>> pet_dog_with_arg.speak()
    ruff
    >>> pet_dog_with_arg.kind
    'canine'
    >>> pet_dog_with_arg.wag()
    /wags tail
    >>> pet_dog_with_arg.name is None
    False

    """
