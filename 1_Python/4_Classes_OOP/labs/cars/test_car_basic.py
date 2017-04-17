"""
Create a class namned 'Vehicle' to pass the tests.
"""

import unittest
from valet import Vehicle
import sys


class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.chevy = Vehicle(color='grey', plate='HBE34R8', doors=3)

    def test_vehicle_creation(self):
        self.assertIsNotNone(self.chevy)
        self.assertEqual(self.chevy.color, 'grey', 'Color attribute not assigned.')
        self.assertEqual(self.chevy.plate, 'HBE34R8', 'Plate number not assigned.')
        self.assertEqual(self.chevy.doors, 3, 'Doors not assignmed.')

    def test_vehicle_str_method(self):
        self.assertEqual(str(self.chevy), 'grey 3 door #HBE34R8')

    def test_vehicle_honking(self):
        result = self.chevy.honk()
        self.assertEqual(result, 'HONK!')
