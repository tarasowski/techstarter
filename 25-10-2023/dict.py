# Dictionary Exercises in Python

# Exercise 1: Create a dictionary representing a person's information and print each key-value pair.
person_info = {"name": "Alice", "age": 30, "city": "New York"}
print("Exercise 1 Result:")
for key, value in person_info.items():
    print(key, ":", value)

# Exercise 2: Given a dictionary of student names and their scores, find and print the highest-scoring student.
student_scores = {"Alice": 95, "Bob": 88, "Charlie": 92, "David": 78}
highest_scorer = max(student_scores, key=student_scores.get)
print("Exercise 2 Result:", highest_scorer)

# Exercise 3: Create a dictionary that maps a product name to its price. Calculate the total cost of a shopping cart.
product_prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0, "date": 1.5}
shopping_cart = {"apple": 5, "banana": 3, "cherry": 2}
total_cost = sum(product_prices[item] * quantity for item, quantity in shopping_cart.items())
print("Exercise 3 Result: Total cost is $", total_cost)

# Exercise 4: Given a list of words, create a dictionary that counts the frequency of each word.
words = ["apple", "banana", "cherry", "apple", "banana", "date"]
word_frequency = {word: words.count(word) for word in set(words)}
print("Exercise 4 Result:", word_frequency)

# Exercise 5: Create a dictionary representing a book's information and print the book's title.
book_info = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "Fiction"}
print("Exercise 5 Result:", book_info["title"])

# Exercise 6: Given a list of sentences, create a dictionary that counts the number of words in each sentence.
sentences = ["This is a sample sentence.", "Count the words in this one."]
sentence_word_count = {sentence: len(sentence.split()) for sentence in sentences}
print("Exercise 6 Result:", sentence_word_count)

# Exercise 7: Create a dictionary with the names of countries and their capital cities. Print all the country names.
country_capitals = {"USA": "Washington D.C.", "France": "Paris", "India": "New Delhi"}
country_names = country_capitals.keys()
print("Exercise 7 Result:", list(country_names))

# Exercise 8: Given a dictionary of fruits and their quantities, add a new fruit and its quantity to the dictionary.
fruit_quantities = {"apple": 5, "banana": 3, "cherry": 2}
new_fruit = "grape"
new_quantity = 4
fruit_quantities[new_fruit] = new_quantity
print("Exercise 8 Result:", fruit_quantities)

# Exercise 9: Create a dictionary representing a playlist and calculate the total duration of the playlist.
playlist = {"song1": 3.5, "song2": 4.2, "song3": 2.8}
total_duration = sum(playlist.values())
print("Exercise 9 Result: Total duration is", total_duration, "minutes")

# Exercise 10: Given a dictionary of students and their exam scores, find and print the names of students who scored above a certain threshold.
student_scores = {"Alice": 92, "Bob": 88, "Charlie": 95, "David": 78}
threshold = 90
high_scorers = [name for name, score in student_scores.items() if score > threshold]
print("Exercise 10 Result: High-scorers:", high_scorers)

