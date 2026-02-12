# Function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Example 1: Function without parameters
def greet():
    print("Hello, World!")


greet()  # Calling the function


def mean(a, b):
    return (a * b) / (a + b)


print(mean(5, 10))  # Calling the function with parameters


# """This function does nothing."""
def dummyFunction():
    pass  # This function does nothing
