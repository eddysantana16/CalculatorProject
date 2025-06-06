from typing import Literal
import pytest
from calculator import add, subtract, multiply, divide, calculate

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 5, 4),
    (1000, 2000, 3000),
])

def test_add(a, b, expected):
    assert add (a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
    (100, 50, 50),
])
def test_subtract(a, b, expected):
        assert subtract (a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (0, 100, 0),
    (-1, -1, 1),
    (10, 10, 100),
    
])
def test_multiply(a, b, expected):
    assert multiply (a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (-9, 3, -3),
    (5, 5, 1),
    (0, 1, 0),
])
def test_divide(a, b, expected):
    assert divide (a, b) == expected
    
def test_divide_by_zero():
    assert divide (5, 0) == "Cannot Divide By Zero! -_-"

@pytest.mark.parametrize("choice, a, b, expected", [
    ("1", 2, 2, 4),
    ("2", 5, 3, 2),
    ("3", 3, 4, 12),
    ("4", 8, 2, 4),
    ("4", 8, 0, "Cannot Divide By Zero! -_-"),
    ("9", 1, 1, "Invalid Choice. Try again! -_-")
])

def test_calculate(choice, a, b, expected):
     assert calculate(choice, a, b) == expected