# List in python
# Lists are ordered, mutable, and allow duplicate elements.
# They are defined using square brackets [].
# Creating a list

my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Accessing elements in a list
print("First element:", my_list[0])  # 1
print("Last element:", my_list[-1])  # 5

# Modifying elements in a list
my_list[2] = 10
print("Modified list:", my_list)  # [1, 2, 10, 4, 5]

# Adding elements to a list
my_list.append(6)
print("List after appending 6:", my_list)  # [1, 2, 10, 4, 5, 6]
my_list.insert(2, 3)
print("List after inserting 3 at index 2:", my_list)  # [1, 2, 3, 10, 4, 5, 6]

# Removing elements from a list
my_list.remove(10)
print("List after removing 10:", my_list)  # [1, 2, 3, 4, 5, 6]
my_list.pop(1)
print("List after popping element at index 1:", my_list)  # [1, 3, 4, 5, 6]

# Length of a list
print("Length of the list:", len(my_list))  # 5

# Iterating through a list
print("Iterating through the list:")
for item in my_list:
    print(item)

# check if an element is in the list
print("Is 4 in the list?", 4 in my_list)  # True
print("Is 10 in the list?", 10 in my_list)  # False

# same thing applied to string
my_string = "Hello, World!"
print("Is 'H' in the string?", "H" in my_string)  # True
print("Is 'z' in the string?", "z" in my_string)

# List Comprehension
# List comprehension is a concise way to create lists.
# Example: Create a list of squares from 0 to 9

squares = [x**2 for x in range(10)]
print("List of squares from 0 to 9:", squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# expression = x
# item = x
# iterable = range(10)
lst = [x for x in range(10)]
print("List with comprehension: lst: ", lst)

# Equivalent to:
nlist = []
for x in range(10):
    nlist.append(x)
print("List with for loop: nlist: ", nlist)

# [ WHAT_TO_APPEND  for LOOP_VARIABLE in SOURCE ] *************XXX************
# [ WHAT_TO_APPEND  for LOOP_VARIABLE in SOURCE if CONDITION ]

lst2 = [x for x in range(10) if x % 2 == 0]
print("List with comprehension of even numbers: ", lst2)
