# # While loop in Python
# # A while loop is used to execute a block of code repeatedly as long as a given condition
# # is true. It is used when the number of iterations is not known beforehand.
# # Example 1: Print numbers from 1 to 5
# # i = 1
# # while i <= 5:
# #     print(i)
# #     i += 1

# # Example 2: Print even numbers from 1 to 10
# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1
# else:
#     print("Loop is over")

# # Do while in Python is not available but we can achieve the same functionality using while loop and break statement.
# # Example 3: Do while loop in Python
# i = 1
# while True:
#     print(i)
#     i += 1
#     if i > 5:
#         break

# # Break and Continue statements in while loop
# # Break statement is used to exit the loop when a certain condition is met.
# # Example 4: Break statement in while loop
# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1

# # Continue statement is used to skip the current iteration and move to the next iteration.
# # Example 5: Continue statement in while loop
# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# print("While with break and continue is over")

# y = 0
# while y <= 12:
#     if y == 10:
#         break
#     y = y + 1
#     print("5 X", y, "", 5 * y)

y = 0
while y <= 10:
    if y == 5:
        print("Skipping the iteration when y", y)
        y += 1
        continue

    print("value of y:", y)

    if y == 10:
        print("Breaking the loop when y = 10", y)
        break
    y += 1

# y = 0

# while y <= 10:
#     if y == 5:
#         print("Skipping the iteration when y = 5", y)
#         y += 1
#         continue

#     print("value of y:", y)

#     if y == 10:
#         print("Breaking the loop when y = 10", y)
#         break

#     y += 1
