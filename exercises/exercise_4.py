# Exercise 4: Create a function to check whether the brackets in a given string are balanced or not.

def are_brackets_balanced(s):
    # Your code here
    open = ["[","{","("]
    close = ["]","}",")"]
    stack = []
    for i in s:
        if i in open:
            stack.append(i)
        elif i in close:
            pos = close.index(i)
            if ((len(stack) > 0) and
                (open[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

            
                

                



# Unit tests
import unittest

class TestExercise4(unittest.TestCase):

    def test_are_brackets_balanced(self):
        self.assertTrue(are_brackets_balanced("({[]})"))
        self.assertFalse(are_brackets_balanced("([)]"))
        self.assertFalse(are_brackets_balanced("{[}"))

if __name__ == '__main__':
    unittest.main()
