class TestAnimals:


    def setup_class(self):
        """
        setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        self.llama = Animal(sound='shazbat')
        self.snake = Animal(legs=0)

    def test_default_animal_creation(self):
        assert self.llama.is_animal is True
        assert self.llama.is_mineral is False
        assert self.is_vegetable is False

    def test_animal_speaking(self):
        assert self.llama.speak() == 'shazbat'
        assert self.snake.speak() is None
