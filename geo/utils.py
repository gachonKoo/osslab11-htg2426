# geo/utils.py
import math

def calculate_area_of_circle(radius):
    if radius <= 0:
        raise ValueError("반지름은 0보다 커야 합니다.")
    return math.pi * (radius ** 2)

def calculate_area_of_rectangle(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("길이와 너비는 0보다 커야 합니다.")
    return length * width
