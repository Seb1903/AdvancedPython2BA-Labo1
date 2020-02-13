# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils
import math 

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0), 1)
    
    def test_roots(self):
        self.assertEqual(utils.roots(5,0,0),0)
    
    def test_integrate(self):
        self.assertAlmostEqual(utils.integrate("x",0,1), 1/2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
