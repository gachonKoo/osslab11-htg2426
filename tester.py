from geo.utils import calculate_circle_area

def test_calculate_circle_area():
    assert calculate_circle_area(1) == 3.141592653589793, "Test failed for radius 1"
    print("Test passed!")

if __name__ == "__main__":
    test_calculate_circle_area()