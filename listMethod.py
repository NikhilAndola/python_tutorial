list = [1, 2, 3, 4, 5]
list.append(2)  # Adding an element to the end of the list
print(list)  # Output: [1, 2, 3, 4, 5, 2]
print(list.count(2))  # Output: 2 (number of occurrences of 2 in the list)

list2 = [2, 3, 4, 10]


def func(x):
    return list2.__contains__(x)


list.sort()  # Sorting the list in ascending order
print("printing list after using sort(): ", list)  # Output: [1, 2, 2, 3, 4, 5]

list.sort(key=func)  # Sorting the list using a custom comparison function
print(list)  # Output: [1, 5, 2, 2, 3, 4] (sorted in order of presence in list2)

listCopy = [1, 2, 2, 3, 6, 3, 4, 5]

set1 = set(listCopy)  # Converting the list to a set to remove duplicates
print("set from listCopy: ", set1)  # Output: {1, 2, 3, 4, 5} (duplicates removed)

plist = [6, 2, 1, 3, 4, 5]
print("index", plist.index(2))
newPList = plist.copy()  # Creating a copy of the list
print("copy of plist", newPList)
newPList.sort()  # Sorting the copied list
print("sorting of plist", newPList)


a = [1, 2, 3, 4, 5]
a.insert(1, 10)
b = [700, 800, 900]
# a.append(b)
a.extend(b)
print(a)

c = [100, 200, 300]

k = b + c
print(k)
