import unittest
from ask2 import is_valid_phone

class CheckNumberTest(unittest.TestCase):
    def test_check_valid(self):
        self.assertTrue(is_valid_phone("+447123456789"))
    def test_check_invalid_1(self):
        self.assertFalse(is_valid_phone("+4472123456789"))
    def test_check_invalid_2(self):
        self.assertFalse(is_valid_phone("+44712345678a"))
        
if __name__ == "__main__":
    unittest.main()