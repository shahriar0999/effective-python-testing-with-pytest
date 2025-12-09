import pytest
from app.calculations import add, subtract, multiply, divide


@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 5),
    (5, 7, 12),
    (0, 0, 0),
    (-1, 1, 0)])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected
    print("Addition test passed.")

def test_subtract():
    assert subtract(5, 3) == 2
    print("Subtraction test passed.")

def test_multiply():
    assert multiply(4, 3) == 12
    print("Multiplication test passed.")

def test_divide():
    assert divide(10, 2) == 5
    print("Division test passed.")