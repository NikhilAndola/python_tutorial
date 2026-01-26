# string in python
# Strings are sequences of characters enclosed within single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

# Strings are immutable, meaning once created, their content cannot be changed.
# Creating strings
str1 = 'Hello, World!'  # single quotes
str2 = "Python is fun."  # double quotes
str3 = '''This is a
multi-line string.'''  # triple single quotes
str4 = """Another
multi-line string."""  # triple double quotes
# Printing strings
print("String 1:", str1)
print("String 2:", str2)
print("String 3:", str3)
print("String 4:", str4)
# Length of a string
print("Length of str1:", len(str1))
# Accessing characters in a string
print("First character of str1:", str1[0])  # H
print("Last character of str1:", str1[-1])  # !
# Slicing strings
print("Substring of str2 (0-6):", str2[0:6])  # Python
print("Substring of str2 (7-end):", str2[7:])  # is fun.
print("Substring of str2:", str2[:5])  # is fun.
print("Substring of str2: (passing : only)", str2[:])  # is fun.


# # iterating through a string
# for char in str1:
#     print(char)

# for i, char in enumerate(str1):
#     print("The index is", i, "value at this index:", char)

# xx = "hello world",
# print("enumeration of xx", enumerate(xx))

# String methods
print("Uppercase str1:", str1.upper())
