class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Create an instance of the Person class
person = Person("Alice", 30)

# When you print the object or convert it to a string, it uses the __str__ method:
print(person)  # This will call the __str__ method of the Person class and print "Alice, 30 years old"

