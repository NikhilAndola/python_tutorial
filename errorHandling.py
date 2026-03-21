a = 10

try:
    print(a / 0)
except ZeroDivisionError as e:
    print("You cannot divide by zero!")
    print("Error details:", e)


# Types of exceptions in Python:
# 1. ZeroDivisionError: Raised when you try to divide a number by zero.
# 2. ValueError: Raised when a function receives an argument of the correct type but an inappropriate value.
# 3. TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# 4. IndexError: Raised when you try to access an index that is out of range in a list or tuple.
# 5. KeyError: Raised when you try to access a key that does not exist in a dictionary.
# 6. FileNotFoundError: Raised when you try to open a file that does not exist.
# 7. ImportError: Raised when an import statement fails to find the module definition or when a from ...import fails to find a name that is to be imported.
# 8. AttributeError: Raised when an attribute reference or assignment fails.
# 9. SyntaxError: Raised when the parser encounters a syntax error.
# 10. NameError: Raised when a local or global name is not found.
# Example of handling multiple exceptions
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a valid number.")
# Example of using finally block
try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("The file does not exist!")
finally:
    print("This block will always be executed, regardless of exceptions.")
