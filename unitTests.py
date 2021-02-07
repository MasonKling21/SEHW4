from cube import *
from List import *
from name import *

import unittest

class TestModules(unittest.TestCase):

    def testCube(self):
        self.assertEqual(volumeOfCube(17), 4913)
        self.assertEqual(volumeOfCube(-32), "Error! Value should be greater than 0.")
        self.assertEqual(volumeOfCube('a'), "Error! Value should be a number.")

    def testList(self):
        self.assertEqual(listAverage([20,21,22]), 21)
        self.assertEqual(listAverage([2]), 2)
        self.assertEqual(listAverage([]), 'Error! Invalid list.')
        self.assertEqual(listAverage([2,3,'a',4]), 'Error! Invalid list.')

    def testName(self):
        self.assertEqual(fullName('Joe', 'Shmo'), 'Joe Shmo')
        self.assertEqual(fullName(4, 'Shmo'), 'Error!')
        self.assertEqual(fullName('Joe', 2), 'Error!')
        self.assertEqual(fullName(5, 2), 'Error!')

if __name__ == '__main__':
    unittest.main()
