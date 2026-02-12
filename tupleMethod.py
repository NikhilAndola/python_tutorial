# Manipulating tuples in python

# Example 1: Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenatedTuple = tuple1 + tuple2
print(concatenatedTuple)  # Output: (1, 2, 3, 4, 5, 6)

# Example 2: Repeating tuples
repeatedTuple = tuple1 * 3
print(repeatedTuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Example 3: Checking for item existence in a tuple
print(2 in tuple1)  # Output: True (checking if 2 is in tuple1)
print(5 in tuple1)  # Output: False (checking if 5 is in tuple1)

# Example 4: Slicing tuples
slicedTuple = concatenatedTuple[2:5]
print(
    slicedTuple
)  # Output: (3, 4, 5) (slicing the concatenated tuple from index 2 to 4)

# Example 5: Finding the index of an item in a tuple
print(tuple1.index(2))  # Output: 1 (finding the index of 2 in tuple1)

# Example 6: Counting occurrences of an item in a tuple
tuple3 = (1, 2, 2, 3, 4, 5)
print(tuple3.count(2))  # Output: 2 (counting the occurrences of 2 in tuple3)

# Example 7: Unpacking tuples
a, b, c = tuple1
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Example 8: Using tuples as dictionary keys
myDict = {("John", "Doe"): "Engineer", ("Jane", "Smith"): "Doctor"}
print(
    myDict[("John", "Doe")]
)  # Output: Engineer (accessing the value using a tuple as a key)
