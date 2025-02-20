from unittest import TestCase
from palindrome_check import is_palindrome

class Test(TestCase):
    def test_palindrome_simple(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome(""))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("Racecar!"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A"))

