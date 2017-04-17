"""
Write a class named 'Vehicle' to pass the unittests.
"""

class Vehicle:

    def __init__(self, color, plate, doors):
        self.color = color
        self.plate = plate
        self.doors = doors

    def __str__(self):
        return "{0.color} {0.doors} door #{0.plate}".format(self)

    def honk(self):
        return 'HONK!'
