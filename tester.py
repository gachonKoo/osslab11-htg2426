# tester.py
import unittest
from geo.utils import calculate_area_of_circle, calculate_area_of_rectangle

class TestGeoFunctions(unittest.TestCase):

    def test_calculate_area_of_circle(self):
        """calculate_area_of_circle 함수 테스트"""
        self.assertAlmostEqual(calculate_area_of_circle(1), 3.141592653589793, places=7)
        self.assertRaises(ValueError, calculate_area_of_circle, -1)
        self.assertRaises(ValueError, calculate_area_of_circle, 0)

    def test_calculate_area_of_rectangle(self):
        """calculate_area_of_rectangle 함수 테스트"""
        self.assertEqual(calculate_area_of_rectangle(2, 3), 6)
        self.assertEqual(calculate_area_of_rectangle(5, 5), 25)
        self.assertRaises(ValueError, calculate_area_of_rectangle, -2, 3)
        self.assertRaises(ValueError, calculate_area_of_rectangle, 2, 0)

if __name__ == '__main__':
    unittest.main()