from app.calculations import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
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