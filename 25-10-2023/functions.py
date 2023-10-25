# Exercise 1: Write a Python function that takes two numbers as input and returns their sum.
def add_numbers(num1, num2):
    return num1 + num2

# Exercise 2: Create a function that calculates the area of a rectangle. It should take the length and width as parameters and return the area.
def calculate_rectangle_area(length, width):
    return length * width

# Exercise 3: Write a function that checks whether a given number is even or odd and returns the result.
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Exercise 4: Create a function that takes a list of numbers as input and returns the sum of all the numbers in the list.
def sum_of_numbers(numbers):
    return sum(numbers)

# Exercise 5: Write a function that takes a string as input and returns the string reversed.
def reverse_string(input_string):
    return input_string[::-1]

# Exercise 6: Create a function that checks if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
def is_palindrome(word):
    return word == word[::-1]

# Exercise 7: Write a function that takes a list of words as input and returns a new list containing the length of each word.
def word_lengths(word_list):
    return [len(word) for word in word_list]

# Exercise 8: Create a function that simulates rolling a six-sided die. It should return a random number between 1 and 6.
import random
def roll_die():
    return random.randint(1, 6)

# Exercise 9: Write a function that calculates the factorial of a given number. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Exercise 10: Create a function that takes a list of numbers as input and returns the largest and smallest numbers in the list.
def find_largest_and_smallest(numbers):
    if not numbers:
        return None, None
    else:
        return max(numbers), min(numbers

# Testing the functions
if __name__ == "__main__":
    # Test the exercises here with sample inputs
    print(add_numbers(5, 3))
    print(calculate_rectangle_area(4, 6))
    print(is_even_or_odd(7))
    print(sum_of_numbers([1, 2, 3, 4, 5]))
    print(reverse_string("hello"))
    print(is_palindrome("racecar"))
    print(word_lengths(["apple", "banana", "cherry"]))
    print(roll_die())
    print(factorial(5))
    print(find_largest_and_smallest([12, 3, 8, 16, 4, 2]))

