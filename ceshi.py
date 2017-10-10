
"""
doctest
"""
# def square(x):
#     """
#     Square a number and returns the result.
#     >>> square(2)
#     4
#     >>> square(3)
#     9
#     """
#     return x * x
#
#
# if __name__ == '__main':
#     import doctest,ceshi
#     doctest.testmod(ceshi)



"""
unittest
"""
import unittest
class ProductTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def testIntegers(self):
        for x in range(-10, 10, 1):
            for y in range(-10, 10, 1):
                p = lambda: 20
                self.failUnless(p == x * y,'Integer multiplication failed')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()












