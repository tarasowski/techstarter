# Exercise 1: Create a list of fruits and print the first fruit in the list.
fruits = ["apple", "banana", "cherry", "date", "fig"]
print("First fruit:", fruits[0])

# Exercise 2: Create a list of numbers and print the last number in the list.
numbers = [1, 2, 3, 4, 5]
print("Last number:", numbers[-1])

# Exercise 3: Create a string and print the third character in the string.
text = "Python"
print("Third character:", text[2])

# Exercise 4: Create a list of colors and print the second and third colors in the list.
colors = ["red", "blue", "green", "yellow", "orange"]
print("Second color:", colors[1])
print("Third color:", colors[2])

# Exercise 5: Create a nested list of items and print the second item from the second list.
nested_list = [[1, 2, 3], ["apple", "banana", "cherry"]]
print("Second item from the second list:", nested_list[1][1])

# Exercise 1: Create a list of numbers and find the sum of all the elements in the list.
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("Sum of numbers:", total)

# Exercise 2: Given a list of numbers, find the average of all the elements in the list.
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print("Average of numbers:", average)

# Exercise 3: Filter a list of words to get only the words with more than three characters.
words = ["apple", "banana", "cat", "dog", "elephant"]
filtered_words = [word for word in words if len(word) > 3]
print("Words with more than three characters:", filtered_words)

# Exercise 4: Reverse a given list.
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print("Reversed list:", reversed_list)

# Exercise 5: Create a list with only the even numbers from a given list of numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

# Exercise 6: Merge two lists into a single sorted list.
list1 = [3, 7, 1, 9]
list2 = [5, 2, 8, 4]
merged_list = sorted(list1 + list2)
print("Merged and sorted list:", merged_list)

# Exercise 7: Find the maximum and minimum elements in a list of numbers.
numbers = [12, 3, 8, 16, 4, 2]
maximum = max(numbers)
minimum = min(numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)

# Exercise 8: Remove duplicates from a list.
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(original_list))
print("List with duplicates removed:", unique_list)

# Exercise 9: Count the number of occurrences of a specific element in a list.
numbers = [1, 2, 3, 2, 4, 2, 5]
count_of_2 = numbers.count(2)
print("Count of 2:", count_of_2)

# Exercise 10: Sort a list of strings in alphabetical order.
fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits.sort()
print("Sorted list of fruits:", fruits)

