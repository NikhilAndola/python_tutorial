# "==" operator checks for value equality,
# while "is" operator checks for identity (whether two variables point to the same object in memory).

a = 5
b = 5
print(a is b)  # Output: True
print(a == b)  # Output: True

c = [1, 2, 3]
d = [1, 2, 3]

print(c is d)  # Output: False
print(c == d)  # Output: True

e = None
f = None
print(e is f)  # Output: True
print(e == f)  # Output: True

g = (3, 4, 5)
h = (3, 4, 5)
print(g is h)  # Output: True
print(g == h)  # Output: True
