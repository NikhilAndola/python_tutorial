# def calculate_percentage(userMarks, totalMarks, numSubjects):
#     """
#     Calculate the percentage of marks obtained by a user.

#     Args:
#         userMarks: List of marks obtained by user in each subject
#         totalMarks: List of total marks for each subject
#         numSubjects: Number of subjects

#     Returns:
#         Percentage of marks obtained
#     """
#     total_obtained = sum(userMarks)
#     total_possible = sum(totalMarks)

#     if total_possible == 0:
#         return 0

#     percentage = (total_obtained / total_possible) * 100
#     return percentage


a = input("Enter your name: ")
print("Hello,", a)


x = input("Enter first Number: ")
y = input("Enter second Number: ")

print(x + y)  # This will concatenate the inputs as strings


# To perform addition, we need to convert the inputs to integers or floats
x = float(x)
y = float(y)
print("Addition:", x + y)
