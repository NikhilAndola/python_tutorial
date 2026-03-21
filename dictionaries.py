# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and does not allow duplicates.
# In Python, dictionaries are written with curly brackets, and they have keys and values.

# Example 1: Creating a dictionary
myDict = {"name": "John", "age": 30, "city": "New York", 235: "id for user"}
print(myDict)  # Output: {'name': 'John', 'age':30, 'city': 'New York'}

print(myDict["name"])  # Output: John
print(myDict["age"])  # Output: 30
print(myDict["city"])  # Output: New York

print(myDict[235])  # Output: id for user
print(myDict.get("age"))  # Output: 30 (using the get() method to access a value)

print(
    myDict.keys()
)  # Output: dict_keys(['name', 'age', 'city', 235]) (getting all keys)
print(
    myDict.values()
)  # Output: dict_values(['John', 30, 'New York', 'id for user']) (getting all values)
print(
    myDict.items()
)  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York'), (235, 'id for user')]) (getting all key-value pairs)


for key in myDict:
    print(key)  # Output: name, age, city, 235 (iterating through keys)

# same as above but using keys() method
for key in myDict.keys():
    print(key)

for value in myDict.values():
    print(value)  # Output: John, 30, New York, id for user (iterating through values)

for key, value in myDict.items():
    print(
        key, value
    )  # Output: name John, age 30, city New York, 235 id for user (iterating through key-value pairs)
