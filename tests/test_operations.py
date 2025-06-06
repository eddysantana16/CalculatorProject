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

##Test

from unittest.mock import patch
import builtins
import calculator

def test_main_quit():
    with patch.object(builtins, 'input', side_effect=["5", "10", "3","4"]):
        calculator.main()

##Test

from unittest.mock import patch
import builtins
import calculator

def test_main_quit_immediately():
    with patch.object(builtins, 'input', side_effect=["5"]):
        calculator.main()

def test_main_add_then_quit():
    with patch("builtins.input", side_effect=["1", "10", "5", "5"]):
        calculator.main()

def test_main_invalid_input_then_quit():
    with patch("builtins.input", side_effect=["1", "ten", "5", "5"]):
        calculator.main()

def test_main_invalid_choice_then_quit():
    with patch("builtins.input", side_effect=["9", "10", "5", "5"]):
        calculator.main()


##Test

from unittest.mock import patch
import builtins
import calculator

def test_main_quit():
    with patch.object(builtins, 'input', side_effect=["5"]):
        calculator.main()

def test_main_valid_addition():
    with patch("builtins.input", side_effect=["1", "2", "3", "5"]):
        calculator.main()

def test_main_invalid_input():
    with patch("builtins.input", side_effect=["1", "abc", "5"]):
        calculator.main()

def test_main_divide_by_zero():
    with patch('builtins.input', side_effect=["4", "10", "0", "5"]):
        calculator.main()

def test_main_invalid_choice():
    with patch("builtins.input", side_effect=["9", "5"]):
        calculator.main()

def test_main_invalid_number_input_loop():
    with patch('builtins.input', side_effect=["1", "abc", "5"]):
        calculator.main()

##Test

from unittest.mock import patch
import calculator

def test_main_all_branches():
    inputs = [
        "1", "10", "5",      
        "2", "20", "5",      
        "3", "3", "3",       
        "4", "8", "2",       
        "9",                 
        "5"                  
    ]
    with patch('builtins.input', side_effect=inputs):
        calculator.main()

