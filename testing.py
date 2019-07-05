# doctest modules is a tool for scanning and validating tests embedded in a
# programs docstrings. Test contruction is simply writing a typical call
# and its results into the docstring

def average(values):
    """Computes the mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

def median(values):
    """Returns the median of a list of numbers

    >>> print(median([20,30,60]))
    30
    """
    import statistics
    return statistics.median(values)


import doctest
doctest.testmod() # automatically validate embedded tests


# unittest allows more comprehensive testing than doctest, and can be
# maintained in a separate file

import unittest

class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

    def test_median(self):
        self.assertEqual(median([20, 30, 60]), 30.0)
        self.assertEqual(median([1, 6, 3, 4, 2]), 3)
        with self.assertRaises(TypeError):
            median(20, 40, 70)

unittest.main() # calling from the command line invokes all tests