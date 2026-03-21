# lambda function in python
# lambda function is a anonymous function which can take any number of arguments but can only have one
# expression. It is used to create small and throwaway functions.
# syntax: lambda arguments: expression

# example 1: lambda function to add two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

quadratic = lambda x: x**2 + 2 * x + 1
print(quadratic(3))  # Output: 16


def double(x):
    return x * 2


double_lambda = lambda x: x * 2
print(double(5))  # Output: 10
print(double_lambda(5))  # Output: 10

# example 2: lambda function to find the maximum of two numbers
max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))  # Output: 20


def argFunc(fx, value):
    return fx(value)


argFunc(lambda x: x * 2, 5)  # Output: 10
