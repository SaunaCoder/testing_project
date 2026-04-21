#!/usr/bin/env python3
"""
Simple script to demonstrate the Password Validator.
"""

from src.validator import PasswordValidator

def main():
    validator = PasswordValidator()

    # Test cases
    test_passwords = [
        "ValidPass123",
        "short",
        "",
        None,
        123,
        "VeryLongPasswordWithAllRequirements123456789"
    ]

    for pwd in test_passwords:
        is_valid, errors = validator.validate(pwd)
        print(f"Password: {repr(pwd)} -> Valid: {is_valid}, Errors: {errors}")

if __name__ == "__main__":
    main()