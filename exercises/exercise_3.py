# Exercise 3: Write a function to find the greatest common divisor (GCD) of two numbers.

def gcd(a, b):
    # Your code here
    if a > b:
        c = b
    if a < b:
        c=a
    d = 1;
    for i in range (1,c+1,1):
        if (a%i == 0) and (b%i == 0):
            d =i;
    return d


# Unit tests
import unittest

class TestExercise3(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(56, 98), 14)
        self.assertEqual(gcd(54, 24), 6)

if __name__ == '__main__':
    unittest.main()
