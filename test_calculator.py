# test_calculator.py

from calculator import multiply, is_prime

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-2, 6) == -12

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(9) is False
