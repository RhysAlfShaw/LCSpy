import src.LCSpy as LCSpy
import unittest

class TestArithmetic(unittest.TestCase):

    def test_cutout_cat(self):
        LCSpy.cutout_2d(190,55) 

if __name__ == '__main__':
    unittest.main()