import unittest
from math_utils import add, multiply


class MathUtilsTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 7), 12)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)


if __name__ == "__main__":
    unittest.main()
