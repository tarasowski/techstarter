# Conditional Statement Exercises in Python

# Exercise 1: Check if a number is positive, negative, or zero.
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Exercise 2: Determine if a person is eligible to vote.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Exercise 3: Check if a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 4: Determine if a character is a vowel or consonant.
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# Exercise 5: Calculate shipping cost based on weight.
weight = float(input("Enter the weight (in kg): "))
if weight <= 10:
    print("Shipping cost is $10.")
else:
    print("Shipping cost is $20.")

# Exercise 6: Check if a year is a leap year.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# Exercise 7: Determine if a student has passed or failed an exam.
score = int(input("Enter your score: "))
if score >= 60:
    print("Pass")
else:
    print("Fail")

# Exercise 8: Check if a number is prime.
num = int(input("Enter a number: "))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")

# Exercise 9: Calculate and display the absolute value of a number.
num = float(input("Enter a number: "))
if num < 0:
    abs_value = -num
else:
    abs_value = num
print("Absolute value:", abs_value)

# Exercise 10: Determine if a triangle is equilateral, isosceles, or scalene.
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

