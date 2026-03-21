# Global Variable
x = 10


def my_function():
    # Local Variable
    y = 5

    global z  # Declaring z as a global variable
    z = 15  # Assigning a value to the global variable z

    print("Inside the function, x =", x)  # Accessing global variable
    print("Inside the function, y =", y)  # Accessing local variable


my_function()
print("Outside the function, x =", x)  # Accessing global variable
# Accessing global variable which was declared inside the function
print("Outside the function, z =", z)
# This will raise an error because y is a local variable
# print("Outside the function, y =", y)
