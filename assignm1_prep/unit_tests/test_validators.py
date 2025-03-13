import unittest
from validators import is_valid_email


class ValidatorsTest(unittest.TestCase):
    def test_is_valid_email_1(self):
        self.assertTrue(is_valid_email("int03063@uoi.gr"))

    def test_is_valid_email_2(self):
        self.assertFalse(is_valid_email("int03"))


if __name__ == "__main__":
    unittest.main()
