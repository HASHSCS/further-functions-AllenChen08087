# Exercise 2: Write a function that accepts a string and returns the longest palindromic substring in that string.

def longest_palindromic_substring(s):
    # Your code here
    def is_palindrome(sub):
        return sub == sub[::-1]

    longest = ""
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring

    return longest

# Unit tests
import unittest

class TestExercise2(unittest.TestCase):

    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring("babad"), "bab")
        self.assertEqual(longest_palindromic_substring("cbbd"), "bb")

if __name__ == '__main__':
    unittest.main()
