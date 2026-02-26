import pytest
from lab1_code import length, digit, upper, special, valid

def test_length():
    assert length("12345678") is True
    assert length("short") is False

def test_digit():
    assert digit("pswd123") is True
    assert digit("pswd") is False

def test_upper():
    assert upper("pswd") is False
    assert upper("PSWD") is True

def test_special():
    assert special("Pass!") is True
    assert special("Pass123") is False

def test_x():
    # Пароль з усіма критеріями має дати 4 бали (x = 4)
    assert valid("Strong!Pass1") == 4

def test_empty():
    with pytest.raises(ValueError) as excinfo:
        valid("")
    assert "pswd cannot be empty!" in str(excinfo.value)