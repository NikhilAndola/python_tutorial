from functools import reduce

# def doubleFx(x):
#     return x * 2


# # Map, Reduce and Filter in Python

# # Map applies a function to all the items in an input list. It returns a new list with the results.

# lst = [1, 2, 3, 4, 5]
# doubleListMap = map(doubleFx, lst)
# print(doubleListMap)  # Output: <map object at 0x7f8c8c8c8c8c>
# print(list(doubleListMap))  # Output: [2, 4, 6, 8, 10]


# # Below are polyfills for the map function in Python.
# # They all achieve the same result but use different approaches.
# def mapFunc(fx, lst):
#     x = []
#     for i in lst:
#         x.append(fx(i))
#     return x


# def map2Func(fx, lst):
#     return [fx(i) for i in lst]


# def map3Func(fx, lst):
#     return list(map(fx, lst))


# def map4Func(fx, lst):
#     for i in lst:
#         yield fx(i)


# # example 1: map function to square all the numbers in a list
# numbers = [1, 2, 3, 4, 5]
# squared = mapFunc(doubleFx, numbers)
# print(squared)  # Output: [2, 4, 6, 8, 10]

# result = map4Func(doubleFx, numbers)
# print(list(result))  # Output: [2, 4, 6, 8, 10]

# Filter in python is used to filter out the elements from a list based on a condition.
# It returns a new list with the elements that satisfy the condition.

# example 2: filter function to filter out the even numbers from a list

# numbers = [1, 2, 3, 4, 5]


# def evenNum(x):
#     return x % 2 == 0


# result = filter(evenNum, numbers)
# print(list(result))  # Output: [2, 4]

# # Polyfill for filter function in python


# def filterFunc(fx, lst):
#     x = []
#     for i in lst:
#         if fx(i):
#             x.append(i)
#     return x


# poly_result_filter = filterFunc(evenNum, numbers)
# print("Polyfill result for filter:", poly_result_filter)  # Output: [2, 4]


# Reduce in python is used to apply a function to all the items in an input list and reduce it to a single value.
# It is part of the functools module.

# example 3: reduce function to find the product of all the numbers in a list
numbers = [1, 2, 3, 4, 5]


def product(x, y):
    return x * y


resultForReduce = reduce(product, numbers)
print(resultForReduce)  # Output: 120
