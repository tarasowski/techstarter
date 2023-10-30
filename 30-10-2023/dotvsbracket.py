# Using Dot Notation

# Define a class with attributes and a method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

# Create an instance of the Person class
person = Person("Alice", 30)

# Accessing object attributes using dot notation
name = person.name  # Access the 'name' attribute
age = person.age    # Access the 'age' attribute

# Calling a method using dot notation
greeting = person.greet()  # Call the 'greet' method

# Using Bracket Notation

# Define a list and a dictionary
my_list = [1, 2, 3, 4, 5]
my_dict = {'name': 'Bob', 'age': 25}

# Accessing elements from a list using bracket notation
index = 2
element = my_list[index]  # Access an element from the list

# Accessing values from a dictionary using bracket notation
key = 'name'
value = my_dict[key]  # Access a value from the dictionary

# Print the results
print(f"Using Dot Notation:")
print(f"Name: {name}, Age: {age}")
print(f"Greeting: {greeting}\n")

print(f"Using Bracket Notation:")
print(f"Element from the list: {element}")
print(f"Value from the dictionary: {value}")


# you can use the .get() method on both dictionaries (dicts) and objects in Python.
my_dict = {'name': 'Alice', 'age': 30}
name = my_dict.get('name', 'Unknown')  # Using .get() to access the 'name' key
city = my_dict.get('city', 'Unknown')  # Using .get() with a default value for a non-existent key

