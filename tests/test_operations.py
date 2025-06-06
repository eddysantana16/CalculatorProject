from calculator import add, subtract, multiply, divide

def test_add():
    assert add (8, 2) == 10
def test_subtract():
    assert subtract (7, 3) == 4
def test_multiply():
    assert multiply (8, 2) == 16
def test_divide():
    assert divide (10, 2) == 5
def test_divide_by_zero():
    assert divide (5, 0) == "Cannot Divide By Zero! -_-"