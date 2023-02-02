import src.LoFAR_cutout as LoFAR_cutout
import unittest

class TestArithmetic(unittest.TestCase):

    def test_cutout_cat(self):
        LoFAR_cutout.cutout_2d(190,55) 

if __name__ == '__main__':
    unittest.main()