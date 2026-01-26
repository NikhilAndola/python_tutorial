# This is variable_and_datatypes.py file.
# variable_and_datatypes.py
# Everything in python is an object, and every object has a data type.

a = 10  # integer variable
b = 3.14  # float variable
c = "Hello"  # string variable
d = True  # boolean variable
e = 6 + 2j  # complex number variable
# printing variable values
print("Integer a:", a)
print("Float b:", b)
print("String c:", c)
print("Boolean d:", d)
print("Complex e:", e)
# checking data types
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))
print("Type of e:", type(e))
# performing basic operations


# Sequenced Data in Python: Lists, Tuples, and Ranges
# List: Mutable ordered collection
# List is a mutable ordered collection of items. Lists are defined using square brackets [] and can contain items of different data types.
my_list = [1, 2, 3, 4, 5, ["apple", "banana"], "toyota car", [-6, 10]]
print("List:", my_list)

# Tuple: Immutable ordered collection
# Tuple is an immutable ordered collection of items. Tuples are defined using parentheses () and can also contain items of different data types.
my_tuple = (10, 20, 30, 40, 50, ("cat", "dog"), "honda bike", [-3, 7])
print("Tuple:", my_tuple)


# Range: Immutable sequence of numbers
# Range represents an immutable sequence of numbers and is commonly used for looping a specific number of times. Ranges are created using the range() function.
my_range = range(1, 11)  # Range from 1 to 10
print("Range:", list(my_range))  # Converting range to list for display

# Mapped data in Python: Dictionaries and Sets
# Dictionary: Key-value pairs
# Dictionary is a collection of key-value pairs. Dictionaries are defined using curly braces {} and allow for fast lookups based on keys.
my_dict = {"name": "Alice", "age": 30, "city": "New York", "canVote": True}
print("Dictionary:", my_dict)
