class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"My name is {self.name}, my age is {self.age}"
    def change_name(self, new_name):
        self.name = new_name
    def change_age(self, new_age):
        self.age = new_age

# Create an instance of the Person class
# object person
person = Person("Alice", 30)
person.change_name("Dimi")
person.change_age(25)

print(person)


