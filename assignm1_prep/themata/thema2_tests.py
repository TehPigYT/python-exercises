import unittest
from thema2 import avg_no_extremes


class TestingAvg(unittest.TestCase):
    def test_avg(self):
        self.assertEqual(avg_no_extremes([4, 2, 6, 5]), 4.5)

    def test_avg2(self):
        self.assertEqual(avg_no_extremes([7, 18]), None)

    def test_avg3(self):
        self.assertEqual(avg_no_extremes([5, 2, 2, 3, 6, 3]), 3.25)

    def test_avg4(self):
        self.assertEqual(avg_no_extremes([6, 8]), None)


if __name__ == "__main__":
    unittest.main()
