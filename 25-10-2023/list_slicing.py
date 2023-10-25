# List Slicing in Python

# Explanation:
# [start:stop:step]
# List slicing allows you to extract specific portions of a list.

# Example list:
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exercise 1: Get the first five elements from my_list using slicing.
exercise1_result = my_list[:5]
print("Exercise 1 Result:", exercise1_result)

# Exercise 2: Get the elements from index 3 to 7 using slicing.
exercise2_result = my_list[3:8]
print("Exercise 2 Result:", exercise2_result)

# Exercise 3: Get every second element from my_list starting from index 2.
exercise3_result = my_list[2::2]
print("Exercise 3 Result:", exercise3_result)

# Exercise 4: Get the last three elements from my_list using negative indices.
exercise4_result = my_list[-3:]
print("Exercise 4 Result:", exercise4_result)

# Exercise 5: Reverse my_list using slicing.
exercise5_result = my_list[::-1]
print("Exercise 5 Result:", exercise5_result)

# Additional Exercises:
# - Create a list of fruits and use slicing to print the first three fruits.
# - Given a list of colors, use slicing to extract all colors except the first and last.
# - Create a string with your name and use slicing to print every other letter.
# - Use list slicing to extract the even numbers from a list of integers.

# You can add these additional exercises to the same file and let your students practice list slicing.

# Exercise 1: Create a list of numbers from 1 to 10 and print every second number.
numbers = list(range(1, 11))
every_second_number = numbers[::2]
print("Every second number:", every_second_number)

# Exercise 2: Create a string and print the characters at even positions.
text = "PythonProgramming"
even_characters = text[1::2]
print("Even-positioned characters:", even_characters)

# Exercise 3: Create a list of fruits and print the list in reverse order using slicing.
fruits = ["apple", "banana", "cherry", "date", "fig"]
reversed_fruits = fruits[::-1]
print("Reversed list of fruits:", reversed_fruits)

# Exercise 4: Create a list of colors and print the list in reverse order, skipping every other color.
colors = ["red", "blue", "green", "yellow", "orange"]
reversed_and_skipped = colors[::-2]
print("Reversed and skipped list of colors:", reversed_and_skipped)

# Exercise 5: Create a string and print the string in reverse order using slicing.
text = "Hello, World!"
reversed_text = text[::-1]
print("Reversed text:", reversed_text)
