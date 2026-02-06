import os

print(os.system("python --version"))


# match case is a new feature in python 3.10 and above which is similar to switch case in other programming languages.
# It is used to match a value against a series of patterns and execute the corresponding block of code.
x = int(input("Enter a number: "))

match x:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2:
        print("Two")
    case _ if x != 30:
        print("Other number")
    case _ if x != 40:
        print("Another number")
    case _:
        print(x)
