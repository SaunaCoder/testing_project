from .logger import setup_logger

logger = setup_logger()

class PasswordValidator:
    """
    A class to validate passwords based on specific rules.
    """

    def validate(self, password):
        """
        Validates the password.

        Args:
            password: The password to validate (should be a string).

        Returns:
            tuple: (is_valid: bool, error_messages: list of str)
        """
        try:
            if not isinstance(password, str):
                logger.error("Invalid input: password must be a string")
                return False, ["Password must be a string"]

            if password is None or password == "":
                logger.error("Invalid input: password is empty or None")
                return False, ["Password cannot be empty"]

            errors = []
            if len(password) < 8:
                errors.append("Password must be at least 8 characters long")
            if not any(c.isupper() for c in password):
                errors.append("Password must contain at least one uppercase letter")
            if not any(c.islower() for c in password):
                errors.append("Password must contain at least one lowercase letter")
            if not any(c.isdigit() for c in password):
                errors.append("Password must contain at least one digit")

            if errors:
                logger.warning(f"Password validation failed: {', '.join(errors)}")
                return False, errors
            else:
                logger.info("Password validation successful")
                return True, []
        except Exception as e:
            logger.error(f"Unexpected error during validation: {str(e)}")
            return False, ["An unexpected error occurred"]