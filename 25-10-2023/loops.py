# Loops and Conditional Statements - Simple Exercises in Python with Lists

# Example 1: Print the numbers from 1 to 5.
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Example 2: Print "Hello, World!" five times using a for loop.
messages = ["Hello, World!"] * 5
for message in messages:
    print(message)

# Example 3: Print even numbers from 2 to 10.
evens = [2, 4, 6, 8, 10]
for num in evens:
    print(num)

# Example 4: Use a while loop to print numbers from 1 to 5.
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# Example 5: Ask the user for their name and greet them.
name = input("What's your name? ")
print("Hello,", name, "!")

# Example 6: Print the message "It's a weekday" for Monday to Friday.
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
day = input("Enter the day of the week: ")
if day in weekdays:
    print("It's a weekday")

# Example 7: Print the message "Even" or "Odd" based on user input.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example 8: Print the first 5 letters of the alphabet using a list and a for loop.
letters = ['a', 'b', 'c', 'd', 'e']
for letter in letters:
    print(letter)

# Example 9: Print a countdown from 10 to 1 using a while loop.
countdown = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
i = 0
while i < len(countdown):
    print(countdown[i])
    i += 1

# Example 10: Use a for loop to print "Yes" five times.
responses = ["Yes"] * 5
for response in responses:
    print(response)
