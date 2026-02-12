# Sets are unordered collections of unique elements.
# They are mutable, meaning you can add or remove elements
# from a set after it has been created. Sets are defined
# using curly braces {} or the set() constructor.

# Creating a set
mySet = {1, 2, 2, 3, 4, 4, 5}
# duplicates will be removed automatically
print(mySet)  # Output: {1, 2, 3, 4, 5}


myset2 = set()
# {} is used to create an empty dictionary, not an empty set.
# To create an empty set, you need to use the set() constructor.

print(type(myset2))


# Accessing elements in a set
# Sets do not support indexing or slicing because they are unordered.
# However, you can check for the presence of an element using the 'in' keyword.

print(3 in mySet)  # Output: True (checking if 3 is in mySet)
print(6 in mySet)  # Output: False (checking if 6 is in mySet)

# Adding elements to a set
mySet.add(6)  # Adding a single element to the set
print(mySet)  # Output: {1, 2, 3, 4, 5, 6}

mySet.update([7, 8, 9])  # Adding multiple elements to the set
print(mySet)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Removing elements from a set
mySet.remove(3)  # Removing a specific element from the set
print(mySet)  # Output: {1, 2, 4, 5, 6, 7, 8, 9}

# Removing an element from the set without
# raising an error if it doesn't exist
mySet.discard(4)
print(mySet)  # Output: {1, 2, 5, 6, 7, 8, 9}

mySet.discard(10)  # Discarding an element that doesn't e xist (no error)
print(mySet)  # Output: {1, 2, 5, 6, 7, 8, 9}

# Set operations
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(setA.union(setB))  # Output: {1, 2, 3, 4, 5, 6} (union of setA and setB)
print(setA.intersection(setB))  # Output: {3, 4} (intersection of setA and setB)
print(
    setA.intersection_update(setB)
)  # Modifying setA to keep only elements that are also in setB
print(
    setA
)  # Output: {3, 4} (setA is now modified to contain only the intersection of setA and setB)
print(setA.difference(setB))  # Output: {1, 2} (elements in setA but not in setB)
# Output: {1, 2, 5, 6} (elements in either setA or setB but not in both)
print(setA.symmetric_difference(setB))

print(setA.issubset(setB))  # Output: False (checking if setA is a subset of setB)
print(setA.issuperset(setB))  # Output: False (checking if setA is a superset of setB)
print(
    setA.isdisjoint(setB)
)  # Output: False (checking if setA and setB have no elements in common)
print(setA.copy())  # Output: {1, 2, 3, 4} (creating a copy of setA)


for value in mySet:
    print(value)  # Output: 1, 2, 5, 6, 7, 8, 9 (iterating through the set)


fruits = {"orange", "apple", "banana"}

print(fruits)
# del fruits  # Deleting the entire set
# print(fruits)  # This will raise an error because the set has been deleted

fruits.clear()  # Removing all elements from the set
print(fruits)  # Output: set() (the set is now empty)

if "orange" in fruits:
    print("orange is in the set")
else:
    print("orange is not in the set")
