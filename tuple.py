# Tuples in python
# A tuple is a collection which is ordered and unchangeable. In Python, tuples are written with round brackets.

# Example 1: Creating a tuple
myTuple = ("apple", "banana", "cherry")
print(myTuple)  # Output: ('apple', 'banana', 'cherry')
# Example 2: Accessing tuple items
print(myTuple[1])  # Output: banana (accessing the second item in the tuple)
# Example 3: Tuples are immutable
# myTuple[1] = "grape"  # This will raise a TypeError
# Example 4: Tuple with one item (note the comma)
singleItemTuple = ("apple",)
print(singleItemTuple)  # Output: ('apple',)
# Example 5: Tuple unpacking
fruit1, fruit2, fruit3 = myTuple
print(fruit1)  # Output: apple
print(fruit2)  # Output: banana
print(fruit3)  # Output: cherry
# Example 6: Nested tuples
nestedTuple = ("apple", ("banana", "cherry"), "grape")
print(nestedTuple)  # Output: ('apple', ('banana', 'cherry'), 'grape')
print(nestedTuple[1])  # Output: ('banana', 'cherry') (accessing the nested tuple)
print(
    nestedTuple[1][0]
)  # Output: banana (accessing the first item of the nested tuple)

print("Length of myTuple: ", len(myTuple))
