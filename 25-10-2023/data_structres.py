# Data Structure Exercises in Python

# Lists

# Exercise 1: Create a list of favorite fruits and print the first and last elements.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Exercise 1: List of Fruits -", fruits[0], "(first) and", fruits[-1], "(last)")

# Explanation: Lists are ordered collections of elements in Python. They allow you to store and manipulate sequences of data. 
# You can access list elements using indexes, and negative indexes count from the end. Lists are useful for tasks like storing 
# similar items and iterating over them.

# Exercise 2: Calculate the sum of all even numbers in a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum(num for num in numbers if num % 2 == 0)
print("Exercise 2: Sum of Even Numbers -", even_sum)

# Explanation: Lists can store data of different types, and you can perform operations like summing up specific elements. In this 
# case, we use a list comprehension to sum even numbers from the list.

# Exercise 3: Create a list of names and sort it in alphabetical order.
names = ["Alice", "Charlie", "Eve", "Bob", "David"]
names.sort()
print("Exercise 3: Sorted Names -", names)

# Explanation: Lists are mutable, meaning you can change their contents. Sorting a list alphabetically is one common use of lists 
# when you need to organize data.

# Exercise 4: Remove duplicates from a list of numbers and print the unique values.
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Exercise 4: Unique Numbers -", unique_numbers)

# Explanation: Lists are flexible for data storage, but they can contain duplicate values. To remove duplicates, we convert the list 
# to a set (which only allows unique values) and then convert it back to a list.

# Exercise 5: Given a list of words, create a new list containing the lengths of each word.
words = ["apple", "banana", "cherry", "date", "elderberry"]
word_lengths = [len(word) for word in words]
print("Exercise 5: Word Lengths -", word_lengths)

# Explanation: Lists are versatile and can store various data types. In this exercise, we create a new list containing the lengths of 
# words from the original list.

# Dictionaries

# Exercise 6: Create a dictionary mapping countries to their capital cities and print the capital of a specific country.
countries_capitals = {"USA": "Washington D.C.", "France": "Paris", "India": "New Delhi"}
country = "India"
capital = countries_capitals[country]
print("Exercise 6: Capital of", country, "-", capital)

# Explanation: Dictionaries are used to store key-value pairs. They provide an efficient way to map one value to another, which is 
# useful for storing information like country-capital pairs.

# Exercise 7: Given a dictionary of student names and their scores, find the student with the highest score.
student_scores = {"Alice": 92, "Bob": 88, "Charlie": 95, "David": 78}
top_student = max(student_scores, key=student_scores.get)
print("Exercise 7: Top Student -", top_student)

# Explanation: Dictionaries are excellent for associative arrays. In this exercise, we use the max function to find the key with the 
# highest value, which is the top student.

# Exercise 8: Create a dictionary representing a person's contact information and add a new contact.
contacts = {"Alice": "alice@email.com", "Bob": "bob@email.com"}
new_contact = {"Charlie": "charlie@email.com"}
contacts.update(new_contact)
print("Exercise 8: Updated Contacts -", contacts)

# Explanation: Dictionaries can efficiently store structured data. You can add or modify entries using the update method, 
# making them valuable for organizing information.

# Exercise 9: Create a dictionary to count word frequency in a sentence.
sentence = "This is a sample sentence. This sentence is an example."
word_frequency = {}
for word in sentence.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1
print("Exercise 9: Word Frequency -", word_frequency)

# Explanation: Dictionaries are often used for frequency analysis. In this exercise, we count the frequency of words in a sentence.

# Exercise 10: Create a dictionary that counts item occurrences in a list.
items = ["apple", "banana", "apple", "cherry", "date", "banana"]
item_counts = {}
for item in items:
    item_counts[item] = item_counts.get(item, 0) + 1
print("Exercise 10: Item Counts -", item_counts)

# Explanation: Dictionaries are essential for counting occurrences of elements in a data structure. They provide a convenient way to 
# keep track of such information.

# Sets

# Exercise 11: Create sets of numbers and find their union and intersection.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
union_set = set1 | set2
intersection_set = set1 & set2
print("Exercise 11 - Union:", union_set)
print("Exercise 11 - Intersection:", intersection_set)

# Explanation: Sets are used for storing unique, unordered elements. They are beneficial for mathematical operations like union and 
# intersection.

# Exercise 12: Check if one set is a subset of another.
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}
is_subset = setA.issubset(setB)
print("Exercise 12: Is setA a subset of setB? -", is_subset)

# Explanation: Sets can be compared for inclusion, making them useful for checking relationships between sets of data.

# Exercise 13: Remove duplicates from a list using a set.
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Exercise 13: Unique Numbers (List) -", unique_numbers)

# Explanation: Sets automatically remove duplicate values, which can be useful for cleaning up lists with repetitive elements.

# Exercise 14: Find elements unique to each set (exclusive OR).
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}
exclusive_elements = (setA | setB) - (setA & setB)
print("Exercise 14: Exclusive Elements -", exclusive_elements)

# Explanation: Sets support set operations like union, intersection, and difference, allowing you to find exclusive elements in this 
# exercise.

# Exercise 15: Find common elements between two lists using sets.
listA = [1, 2, 3, 4, 5]
listB = [3, 4, 5, 6, 7]
common_elements = list(set(listA) & set(listB))
print("Exercise 15: Common Elements -", common_elements)

# Explanation: Sets are efficient for finding common elements between two data structures. Here, we convert lists to sets for 
# intersection.

# Tuples

# Exercise 16: Create a tuple with days of the week and access the third element.
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
third_day = days_of_week[2]
print("Exercise 16: Third Day of the Week -", third_day)

# Explanation: Tuples are similar to lists but are immutable. They are useful for situations where you want to store 
# unchangeable data.

# Exercise 17: Calculate the distance between two coordinates (x1, y1) and (x2, y2).
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

point1 = (1, 2)
point2 = (4, 6)
dist = distance(point1, point2)
print("Exercise 17: Distance -", dist)

# Explanation: Tuples can be used to represent coordinates and other ordered data. In this exercise, we calculate the distance 
# between two points.

# Exercise 18: Calculate the area of a rectangle using a tuple for dimensions (length, width).
dimensions = (4, 5)
area = dimensions[0] * dimensions[1]
print("Exercise 18: Rectangle Area -", area)

# Explanation: Tuples are suitable for situations where data should remain constant. In this exercise, we use a tuple to store the 
# dimensions of a rectangle.

# Exercise 19: Create a tuple with the names of three friends and print them in reverse order.
friends = ("Alice", "Bob", "Charlie")
reverse_friends = friends[::-1]
print("Exercise 19: Reverse Order of Friends -", reverse_friends)

# Explanation: Tuples can hold elements in an ordered fashion. Reversing a tuple is useful for cases where you need data in the 
# opposite order.

# Exercise 20: Given a list of tuples containing names and ages, sort the list by age in ascending order.
people = [("Alice", 28), ("Bob", 22), ("Charlie", 32), ("David", 25)]
sorted_people = sorted(people, key=lambda x: x[1])
print("Exercise 20: Sorted People -", sorted_people)

# Explanation: Tuples can be part of more complex data structures like lists. In this exercise, we sort a list of tuples by a 
# specific element (age).
