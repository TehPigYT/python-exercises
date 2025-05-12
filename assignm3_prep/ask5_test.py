import ask5
import unittest


class TestDistance(unittest.TestCase):
    def test_distance(self):
        self.assertAlmostEqual(ask5.distance((3, 4), (7, 8.1)), 5.728, places=3)


if __name__ == "__main__":
    unittest.main()
