import pytest
from src.validator import PasswordValidator

@pytest.fixture
def validator():
    """Fixture to create a PasswordValidator instance."""
    return PasswordValidator()

@pytest.mark.parametrize("password,expected", [
    # Valid password
    ("ValidPass123", (True, [])),
    # Invalid: too short
    ("Short1a", (False, ["Password must be at least 8 characters long"])),
    # Invalid: no uppercase
    ("nouppercase1", (False, ["Password must contain at least one uppercase letter"])),
    # Invalid: no lowercase
    ("NOLOWERCASE1", (False, ["Password must contain at least one lowercase letter"])),
    # Invalid: no digit
    ("NoDigitsAbc", (False, ["Password must contain at least one digit"])),
    # Invalid: empty string
    ("", (False, ["Password cannot be empty"])),
    # Invalid: None
    (None, (False, ["Password must be a string"])),
    # Invalid: non-string
    (123, (False, ["Password must be a string"])),
    # Valid: very long password
    ("VeryLongPasswordWithAllRequirements123456789", (True, [])),
    # Invalid: multiple violations
    ("short", (False, ["Password must be at least 8 characters long", "Password must contain at least one uppercase letter", "Password must contain at least one digit"])),
])
def test_validate(validator, password, expected):
    result = validator.validate(password)
    assert result == expected