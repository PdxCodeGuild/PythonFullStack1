import unittest
from valet import Vehicle, ParkingLot


class TestValet(unittest.TestCase):

    def setUp(self):
        """
        Create a few instances before we start testing.
        """
        self.mikes_lot = ParkingLot(capacity=3, rate=20.0)
        self.mustang = Vehicle(color='red', plate='PDXFTW')
        self.honda = Vehicle(color='cyan', plate='EWR456')
        self.lemon = Vehicle(color='black', plate='HGH72L')

    def test_initial_lot_creation(self):
        """Ensure that we can initialize the Parking Lot Object correctly."""
        self.assertIsNotNone(self.mikes_lot)
        self.assertEqual(self.mikes_lot.capacity, 3)
        self.assertEqual(self.mikes_lot.available_spaces, self.mikes_lot.capacity)
        self.assertEqual(self.mikes_lot.available_spaces, 3)
        self.assertEqual(self.mikes_lot.hourly_rate, 20.0)

    def test_initial_vehicle_creation(self):
        """Ensure Vehicles can be created correctly"""
        self.assertIsNotNone(self.lemon)
        self.assertEqual(self.lemon.color, 'black')
        self.assertEqual(self.lemon.plate, 'HGH72L')

    def test_lot_available_space_tracking(self):
        """Ensure we are tracking space availabilty correctly."""
        self.assertEqual(self.mikes_lot.available_spaces, self.mikes_lot.capacity)
        self.assertEqual(self.mikes_lot.available_spaces, 3)
        self.mikes_lot.park(self.mustang)
        self.assertNotEqual(self.mikes_lot.available_spaces, 3)
        self.assertEqual(self.mikes_lot.available_spaces, 2)

    def test_vehicle_park(self):
        """Park the car"""
        self.assertEqual(self.mikes_lot.available_spaces, self.mikes_lot.capacity)
        self.assertEqual(self.mikes_lot.available_spaces, 3)
        self.mikes_lot.park(self.mustang)

    def test_filling_lot_to_full_capacity(self):
        """Pack 'em in!"""
        self.mikes_lot.park(self.mustang)
        self.mikes_lot.park(self.honda)
        self.mikes_lot.park(self.lemon)

        delaurean = Vehicle(color='invisible', plate='FUTURE')
        self.assertEqual(self.mikes_lot.park(delaurean), False)

    def test_vehicle_pickup(self):
        """Go get the car"""
        pass
