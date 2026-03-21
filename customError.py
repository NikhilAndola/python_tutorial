# Custom Error in python:
class CustomError(Exception):
    """Custom exception for specific error handling."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Example of raising a custom error
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age < 18:
        raise CustomError("You must be at least 18 years old!")
    else:
        print("Age is valid.")


# Testing the custom error
try:
    validate_age(5)
except CustomError as e:
    print("Custom Error:", e.message)
