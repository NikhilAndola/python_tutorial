# Enumerate function example in python

# Enumerate is a built-in function in Python that allows you to loop over an iterable and have an automatic counter.
# It returns an enumerate object which contains pairs of index and value from the iterable.

# Using enumerate to get index and value from a list
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Using enumerate with a starting index
for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")
