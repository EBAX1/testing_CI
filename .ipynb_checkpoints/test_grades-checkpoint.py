import unittest
import grades as gd

class TestAdd(unittest.TestCase):

    def test_gradeCalculator(self): # test routine
        self.assertEqual(gd.gradeCalculator(90), 'A')
        self.assertEqual(gd.gradeCalculator(80), 'B')
        self.assertEqual(gd.gradeCalculator(70), 'C')
        self.assertEqual(gd.gradeCalculator(60), 'D')
    
unittest.main()