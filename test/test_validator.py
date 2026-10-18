# tests/test_validator.py

from validator import validate_email, validate_phone

def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False
from validator import validate_phone

def test_phone_valid():
    assert validate_phone('89991234567') is True