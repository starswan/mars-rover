import unittest
from Rover import *

class RoverTest(unittest.TestCase):
    def test_rover_move(self):
        p = Plateau(5, 5)
        r = p.addRover(1, 2, 'N', 'LMLMLMLMM')
        self.assertEqual('N', r.facing)
        self.assertEqual(1, r.x)
        self.assertEqual(3, r.y)

    def test_rover_move2(self):
        p = Plateau(5, 5)
        r = p.addRover(3, 3, 'E', 'MMRMMRMRRM')
        self.assertEqual('E', r.facing)
        self.assertEqual(5, r.x)
        self.assertEqual(1, r.y)

    def test_rover_outside_plateau(self):
        p = Plateau(3, 5)
        self.assertEqual(None, p.addRover(-1, 0, 'E', ''))
        self.assertEqual(None, p.addRover(0, -1, 'E', ''))
        self.assertEqual(None, p.addRover(0, 6, 'E', ''))
        self.assertEqual(None, p.addRover(4, 5, 'E', ''))

    def test_rover_plateau_edge(self):
        p = Plateau(3, 5)
        r = p.addRover(0, 5, 'E', '')
        self.assertEqual(0, r.x)
        self.assertEqual(5, r.y)

    def test_drive_over_right_cliff(self):
        p = Plateau(3, 5)
        r = p.addRover(3, 5, 'E', 'M')
        self.assertEqual(3, r.x)
        self.assertEqual(5, r.y)

    def test_drive_over_top_cliff(self):
        p = Plateau(3, 5)
        r = p.addRover(3, 5, 'N', 'M')
        self.assertEqual(3, r.x)
        self.assertEqual(5, r.y)

    def test_drive_over_left_cliff(self):
        p = Plateau(3, 5)
        r = p.addRover(0, 0, 'W', 'M')
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)

    def test_drive_over_lower_cliff(self):
        p = Plateau(3, 5)
        r = p.addRover(0, 0, 'S', 'M')
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)

    def test_drop_two_rovers_on_top(self):
        p = Plateau(3, 5)
        r = p.addRover(0, 0, 'N', '')
        self.assertEqual(None, p.addRover(0, 0, 'N', ''))

    def test_crash_into_each_other(self):
        p = Plateau(3, 5)
        p.addRover(0, 1, 'N', '')
        r = p.addRover(0, 0, 'N', 'M')
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)

    def test_invalid_command(self):
        p = Plateau(3, 5)
        r = p.addRover(0, 1, 'N', 'X')
        self.assertEqual(0, r.x)
        self.assertEqual(1, r.y)


if __name__ == '__main__':
    unittest.main()
