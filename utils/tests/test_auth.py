import unittest
from auth import valid_email


class TestAuth(unittest.TestCase):
    def test_valid_email(self):
        # Valid email addresses
        self.assertTrue(valid_email("test@example.com"))
        self.assertTrue(valid_email("user123@gmail.com"))
        self.assertTrue(valid_email("john.doe@company.co"))

    def test_invalid_email(self):
        # Invalid email addresses
        self.assertFalse(valid_email("test@example"))
        self.assertFalse(valid_email("user123@gmail"))
        self.assertFalse(valid_email("john.doe@company"))

    def test_empty_email(self):
        # Empty email
        self.assertFalse(valid_email(""))

    def test_whitespace_email(self):
        # Email with only whitespace characters
        self.assertFalse(valid_email("   "))


if __name__ == "__main__":
    unittest.main()


