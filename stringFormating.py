letter = "my name is {} and i am {} years old"
name = "Nikhil"
age = 29

letter.format(name, age)
# Output: 'my name is Nikhil and i am 25 years old'
print(letter.format(name, age))


# Same thing can be achieved using f-string:

fstring = f"my name is {name} and i am {age} years old"
print("using fstring", fstring)

price = 25.22222467
# Using format to round the price to 2 decimal places
formatted_price = f"price of thing is {price:.2f}"
print(formatted_price)
