# Typecasting in python
# Typecasting is the process of converting one data type to another.
# There are two types of typecasting: implicit and explicit.

# Implicit Typecasting
# Python automatically converts one data type to another without user intervention.
a = 10  # integer
b = 3.14  # float
c = a + b  # implicit conversion from int to float
print("Implicit Typecasting:", c)

# Explicit Typecasting
# User manually converts one data type to another using built-in functions.
d = "123"  # string
e = int(d)  # explicit conversion from string to integer
print("Explicit Typecasting:", e)

# Types of Typecasting Functions
# int(): Converts a value to an integer
f = 9.99
print("float to int:", int(f))
# float(): Converts a value to a float
g = 10
print("int to float:", float(g))
# str(): Converts a value to a string
h = 100
print("int to str:", str(h))
# list(): Converts a value to a list
i = (1, 2, 3)
print("tuple to list:", list(i))
# tuple(): Converts a value to a tuple
j = [4, 5, 6]
print("list to tuple:", tuple(j))
# set(): Converts a value to a set
k = [1, 2, 2, 3, 4]
print("list to set:", set(k))
# dict(): Converts a value to a dictionary
l = [("name", "Bob"), ("age", 25)]
print("list to dict:", dict(l))
# complex(): Converts a value to a complex number
m = 5
print("int to complex:", complex(m))
# bool(): Converts a value to a boolean
n = 0
print("int to bool:", bool(n))  # 0 is False, non-zero is True
# chr(): Converts an integer to its corresponding Unicode character
o = 65
print("int to char:", chr(o))
# ord(): Converts a character to its corresponding integer Unicode code point
p = 'A'
print("char to int:", ord(p))
# bytes(): Converts a string to bytes
q = "hello"
print("str to bytes:", bytes(q, 'utf-8'))
# bytearray(): Converts a string to a bytearray
r = "world"
print("str to bytearray:", bytearray(r, 'utf-8'))

# frozenset(): Converts a list to a frozenset (immutable set)
s = [1, 2, 3, 4]
print("list to frozenset:", frozenset(s))
# memoryview(): Creates a memory view object from a bytes object
t = b"example"
print("bytes to memoryview:", memoryview(t))

# Note: Not all typecasting functions are applicable to all data types.
# For example, converting a complex number to an integer directly is not allowed and will raise an error.

# Typecasting with Error Handling
# It's good practice to handle potential errors during typecasting.
u = "abc"       # invalid string for int conversion
try:
    v = int(u)
    print("Converted value:", v)
except ValueError:
    print("Error: Cannot convert", u, "to an integer.")
# Similarly, we can handle other typecasting errors as needed.
# Summary
# Typecasting is essential for data manipulation and ensuring compatibility between different data types in Python.
# Python provides various built-in functions for typecasting, and it's important to use them appropriately while handling potential errors.
# Always refer to the official Python documentation for more details on typecasting and data types.
# Official Python Documentation: https://docs.python.org/3/library/functions.html

# End of typecasting.py file.
