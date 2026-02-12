# Argument in function / Required arguments
def add(a, b):
    return a + b


# default parameter/optional parameter/argument with default value


def greet(name="World"):
    print(f"Hello, {name}!")


greet()  # Using default parameter
greet("Alice")  # Overriding default parameter


# keyword arguments
def describe_person(name, age):
    print(f"{name} is {age} years old.")


describe_person(name="Bob", age=30)  # Using keyword arguments
describe_person(age=25, name="Charlie")  # Using keyword arguments in different order
describe_person("Dave", 40)  # Using positional arguments


# Arbitrary number of arguments
def sum_all(*args):
    print("Arguments received:", args)
    return sum(args)


print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(4, 5, 5, 5, 5))  # Output: 9


# Argument as dictionary
def print_info(**kwargs):
    print("Keyword arguments received:", kwargs)


print_info(
    name="Alice", age=30, city="New York"
)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
