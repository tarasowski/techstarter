# List Comprehension Examples in Python

# [ausdruck for element in liste]
# Example 1: Create a list of squares of numbers from 1 to 10.
squares = [x ** 2 for x in range(1, 11)]
print("Example 1:", squares)

# Example 2: Create a list of even numbers from 1 to 20.
def check_if_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

even_numbers = [num for num in range(1, 21) if check_if_even(num)]
print("Example 2:", even_numbers)

# Example 3: Generate a list of uppercase versions of words in a list.
words = ["apple", "banana", "cherry"]
for_uppercase = []
for word in words:
    for_uppercase.append(word.upper())
    
uppercase_words = [word.upper() for word in words]
print("Example 3", for_uppercase)
print("Example 3:", uppercase_words)

# Example 4: Create a list of the lengths of words in a list.
words = ["cat", "elephant", "dog"]

for_word_length = []
for word in words:
    for_word_length.append(len(word))

word_lengths = [len(word) for word in words]
print("Example 4:", word_lengths)

# Example 5: Extract the consonants from a given word.
word = "hello"
consonants = [char for char in word if char not in "aeiou"]
print("Example 5:", consonants)

# Example 6: Create a list of the square roots of positive numbers in another list.
numbers = [25, 16, 9, 4]
square_roots = [x**0.5 for x in numbers if x > 0]
print("Example 6:", square_roots)

# Example 7: Create a list of the first letter of each word in a sentence.
sentence = "This is a sample sentence:"
sentence_splitted = sentence.split()
first_letters = [word[0] for word in sentence_splitted]
last_letters = [word[-1] for word in sentence_splitted if word[-1] not in ".!?:"]
last_letters_isalnum = [word[-1] for word in sentence_splitted if word[-1].isalnum()]
print("Example 7 (first_letter):", first_letters)
print("Example 7 (last_letter):", last_letters)
print("Example 7 (last_letters_islanum):", last_letters_isalnum)

# Example 8: Filter a list of numbers to get only the prime numbers.
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = [x for x in numbers if all(x % i != 0 for i in range(2, x))]
print("Example 8:", prime_numbers)

# Example 9: Create a list of pairs (tuples) with the index and value of each element in a list.
elements = ["apple", "banana", "cherry"]
indexed_elements = [(index, value) for index, value in enumerate(elements)]
print("Example 9:", indexed_elements)

# Example 10: Create a list of words that contain the letter 'a' from a list of words.
words = ["apple", "banana", "cherry", "date"]
a_words = [word for word in words if "a" in word]
print("Example 10:", a_words)


test = {"age": 39, "name": "Dimi"}

for idx, key in enumerate(test):
    print(idx, key)