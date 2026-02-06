# python string methods

sample_string = "  Hello, Python String Methods!  "
print("Original String:", repr(sample_string))
# 1. Strip whitespace
stripped_string = sample_string.strip()
print("Stripped String:", repr(stripped_string))
# 2. Lowercase
lowercase_string = stripped_string.lower()
print("Lowercase String:", repr(lowercase_string))
# 3. Replace substring
replaced_string = lowercase_string.replace("python", "Java")
print("Replaced String:", repr(replaced_string))

# 4. Find substring
index_of_java = replaced_string.find("Java")
print("Index of 'Java':", index_of_java)

# 5. Split string
split_string = replaced_string.split(" ")
print("Split String:", split_string)

# 6. Join list into string
joined_string = "-".join(split_string)
print("Joined String:", repr(joined_string))

# 7. Check if string starts with a substring
starts_with_hello = replaced_string.startswith("hello")
print("Starts with 'hello':", starts_with_hello)

# 8. Check if string ends with a substring
ends_with_methods = replaced_string.endswith("methods!")
print("Ends with 'methods!':", ends_with_methods)

# 9. Count occurrences of a substring
count_of_l = replaced_string.count("l")
print("Count of 'l':", count_of_l)

# 10. Capitalize string
capitalized_string = replaced_string.capitalize()
print("Capitalized String:", repr(capitalized_string))

# 11. Title case
title_case_string = replaced_string.title()
print("Title Case String:", repr(title_case_string))

# 12. Center string
centered_string = replaced_string.center(50, "*")
print("Centered String:", repr(centered_string))

# 13. Check if all characters are alphabetic
is_alpha = replaced_string.replace(" ", "").isalpha()
print("Is alphabetic (ignoring spaces):", is_alpha)

# 14. Check if all characters are digits
is_digit = "12345".isdigit()
print("Is '12345' all digits?:", is_digit)

# 15. Format string
name = "Alice"
age = 30
formatted_string = "Name: {}, Age: {}".format(name, age)
print("Formatted String:", repr(formatted_string))

# 16. Reverse a string using slicing
reversed_string = replaced_string[::-1]
print("Reversed String:", repr(reversed_string))

# 17. Count words in a string
word_count = len(replaced_string.split())
print("Word Count:", word_count)

# 18. Check if string is numeric
is_numeric = "12345.67".isnumeric()
print("Is '12345.67' numeric?:", is_numeric)

# 19. Expand tabs
tabbed_string = "Hello\tWorld"
expanded_string = tabbed_string.expandtabs(4)
print("Expanded Tabs String:", repr(expanded_string))

# 20. Swap case
swapped_case_string = replaced_string.swapcase()
print("Swapped Case String:", repr(swapped_case_string))
