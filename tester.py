# tester.py
import unittest
from geo.utils import calculate_area_of_circle, calculate_area_of_rectangle

class TestGeoFunctions(unittest.TestCase):

    def test_calculate_area_of_circle(self):
        """calculate_area_of_circle 함수 테스트"""
        radius = 5  # 반지름을 5로 설정
        area = calculate_area_of_circle(radius)
        c = radius  # c 값은 반지름
        print(f"c = {c}")  # 'c = 5.0' 출력
        print(f"area = {area}")  # 'area = 314.1592653589793' 출력
        self.assertAlmostEqual(area, 3.141592653589793 * (radius ** 2), places=7)
        self.assertRaises(ValueError, calculate_area_of_circle, -1)
        self.assertRaises(ValueError, calculate_area_of_circle, 0)

    def test_calculate_area_of_rectangle(self):
        """calculate_area_of_rectangle 함수 테스트"""
        length, width = 2, 3
        area = calculate_area_of_rectangle(length, width)
        print(f"c = {length}")  # 'c = 2' 출력
        print(f"area = {area}")  # 'area = 6' 출력
        self.assertEqual(area, 6)
        self.assertRaises(ValueError, calculate_area_of_rectangle, -2, 3)
        self.assertRaises(ValueError, calculate_area_of_rectangle, 2, 0)

if __name__ == '__main__':
    unittest.main()
