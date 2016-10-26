import unittest


class TestAccountCreation(unittest.TestCase):
    def setUp(self):
        self.test_waypoint1 = Waypoint(180)
        self.test_waypoint2 = Waypoint(181)

    def test_initial_waypoint_creation(self):
        self.assertIsNotNone(self.test_waypoint1)
        self.assertIsInstance(obj=self.test_waypoint1, waypoint)
        self.assertEqual(self.test_waypoint1._degrees, 360)
        self.assertEqual(self.test_waypoint1, 270)
        self.assertNotEqual(self.test_Waypoint1._degrees, 0)
