# geo/utils.py

import math

def calculate_area_of_circle(radius):
    """주어진 반지름을 이용해 원의 넓이를 계산하는 함수"""
    if radius <= 0:
        raise ValueError("반지름은 0보다 커야 합니다.")
    return math.pi * (radius ** 2)

def calculate_area_of_rectangle(length, width):
    """주어진 길이와 너비를 이용해 사각형의 넓이를 계산하는 함수"""
    if length <= 0 or width <= 0:
        raise ValueError("길이와 너비는 0보다 커야 합니다.")
    return length * width