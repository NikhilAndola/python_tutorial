import random

# Creating a kbc game using python:
print("Welcome to KBC Game")

questions = [
    "What is the capital of India?",
    "What is the national animal of India?",
    "What is the national bird of India?",
    "What is the national flower of India?",
]
options = [
    ["a. New Delhi", "b. Mumbai", "c. Kolkata", "d. Chennai"],
    ["a. Lion", "b. Tiger", "c. Elephant", "d. Peacock"],
    ["a. Peacock", "b. Sparrow", "c. Crow", "d. Parrot"],
    ["a. Lotus", "b. Rose", "c. Sunflower", "d. Marigold"],
]
answers = ["a", "b", "a", "a"]
score = 0

# for i in range(len(questions)):
#     print(questions[i])
#     for option in options[i]:
#         print(option)
#     user_answer = input("Enter your answer (a/b/c/d): ")
#     if user_answer.lower() == answers[i]:
#         print("Correct!")
#         score += 1
#     else:
#         print("Wrong! The correct answer is:", answers[i])
#     print()

# for i in range(len(questions)):
#     print(questions[i])
#     for option in options[i]:
#         print(option)
#     use_answer = input("Enter your answer (a/b/c/d): ")
#     if use_answer.lower() == answers[i]:
#         print("Correct!")
#         score += 1
#     else:
#         print("Wrong! The correct answer is:", answers[i])

# print("Your final score is:", score)

# for option in options[0]:
#     print(option)

# For random questions:

random_question_index = random.randint(0, len(questions) - 1)
print(random_question_index)

already_asked = set()
for i in range(len(questions)):
    print(already_asked)
    random_question_index = random.randint(0, len(questions) - 1)
    print(
        "check for ",
        random_question_index,
        " in already_asked: ",
        random_question_index in already_asked,
    )
    while random_question_index in already_asked:
        random_question_index = random.randint(0, len(questions) - 1)
    already_asked.add(random_question_index)
    print(questions[random_question_index])
    for option in options[random_question_index]:
        print(option)
    use_answer = input("Enter your answer (a/b/c/d): ")
    if use_answer.lower() == answers[random_question_index]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is:", answers[random_question_index])

print("Your final score is:", score)
