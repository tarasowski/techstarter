# Exercise 1: Create a list of fruits and print the first fruit in the list.
fruits = ["apple", "banana", "cherry", "date", "fig"]
print("first fruit: ", fruits[0])
print("last fruit: ", fruits[-1])

# Exercise 2: Create a list of numbers and print the last number in the list.
numbers = [1, 2, 3, 4, 5]
print(max(numbers))
print(numbers[-2])
# extra: create a list with 100 items
    #print(list(range(1, 101)))

# Exercise 3: Create a string and print the third character in the string.
text = "Python"
print(text[2])

# Exercise 4: Create a list of colors and print the second and third colors in the list.
# Extra: print the second and the fourth ?
colors = ["red", "blue", "green", "yellow", "orange"]
print("colors", colors[1:3])
print(colors[1], colors[3])

# Exercise 5: Print the second item from the second list.
nested_list = [[1, 2, 3], ["apple", "banana", "cherry"]]
print("second items from the second list", nested_list[1][1])
# Extra entpacke die beiden nested lists inside the nested_list into a single simple list
simple_list = nested_list[0] + nested_list[1]
print("flat operation: ", simple_list)


# Exercise 1: Create a list of numbers and find the sum of all the elements in the list.
numbers = [1, 2, 3, 4, 5]
numbers_sum = sum(numbers)
print("sum of numbers in the list", numbers_sum)
# extra make a sum without the built-in sum function in python
summe = 0
for element in numbers:
    summe += element
print("meine summe", summe)

# Exercise 2: Given a list of numbers, find the average of all the elements in the list.
from statistics import mean
numbers = [10, 20, 30, 40, 50]
n_avg = int(sum(numbers) / len(numbers))
print("numbers average", n_avg)
print("from statics module mean aka avg", mean(numbers))

# Exercise 3: Filter a list of words to get only the words with more than three characters.
words = ["apple", "banana", "cat", "dog", "elephant"]
new_words = [word for word in words if len(word) > 3] # list comprehensions
print("list comprehension", new_words)

# create a simple for loop to get the same result as Enrico's proposal
new_words2 = []
for word in words:
    if len(word) > 3:
        new_words2.append(word)

print("a normal for loop", new_words2)

# Exercise 4: Reverse a given list.
original_list = [1, 2, 3, 4, 5]
print("reversed_list", original_list[::-1])

# Exercise 5: Create a list with only the even numbers from a given list of numbers.
# gerade Zahlen vs. ungerade Zahlen
numbers = [1, 2, 33, 32, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 16]
even_numbers = [num for num in numbers if num % 2 == 0]
print("list comprehension: ", even_numbers)

even_numbers2 = []
for num in numbers:
    if num % 2 == 0:
        even_numbers2.append(num)

print("for loop:", even_numbers2)




# Exercise 6: Merge two lists into a single sorted list.
list1 = [3, 7, 1, 9]
list2 = [5, 2, 8, 4]

# Exercise 7: Find the maximum and minimum elements in a list of numbers.
numbers = [12, 3, 8, 16, 4, 2]

# Exercise 8: Remove duplicates from a list.
original_list = [1, 2, 2, 3, 4, 4, 5]

# Exercise 9: Count the number of occurrences of a specific element in a list.
numbers = [1, 2, 3, 2, 4, 2, 5]

# Exercise 10: Sort a list of strings in alphabetical order.
fruits = ["apple", "banana", "cherry", "date", "fig"]

