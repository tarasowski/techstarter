import os # is a built-in python module
import json # is a built-in python json module

# JSON.stringify({name: "Abi"})

obj_encoded = json.dumps({"name": "Abi"}) # von python object zu json string
obj_decoded = json.loads(obj_encoded) # von json zu einem python object

print(obj_decoded)

TEST = os.environ.get("TEST")
REGION = os.environ.get("AWS_REGION")

print(TEST)
print(REGION)

#print("Hallo Welt!")
#name = input("Dein name: ")
#print("Dein Name: ", name)

#print("first"); print("second")
# new line is wichtig und kein Semikolon
print("first")
print("second")

'''
in der Regel werden solche Sachen für Kommentare 
[1, 2, 3, 4] 
    .map(x => x) 
    .filter(x => x) 
    .reverse() 
'''

sum = 2 \
       + 3 \
       + 4 \


# everything that is inside of () is evaluated as an expression
sum2 = (
    2 +
    3 +
    4
)
print("this is my sum: ", sum)
print("this is my sum2: ", sum2)

print("Starte die Anweisung")
a = -10
if a > 0:
    print("hier soll etwas passieren")
    print("a is positive")
    if a > 0:
        print("hier soll")
        print("hier soll")
        if a > 0:
            print("hier ")
            print("hier")
print("new line")
print("Ende die Anweisung")

def main(param1):
    return "Hello from main " + param1

print(
    main("mein first argument")
)

xs = [1, 2, 3, 5]

xs2 = [
        {"name": "Pablo", "age": 35}
      ]


print(
    max([1, 3, 4, 5]),
    min([1, 2, 3, 4])
)

fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print("this are my fruits: ", x)

class Person:
  # similar to javascript constructor
  def __init__ (self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36) # no need for a new keywords as in js
print(p1)
print(p1.name)
print(p1.age)

obj = {"name": "Dimi", "age": 35}

print(obj["name"])
print(obj["age"])
print(obj.get("name", "Pablo"))

"""
this is my multi-line comment
"""

'''
this is my multi-line comment
'''

mal = 5 * 5
geteilt = 5 / 5
res = (3 + 5) * 4

print(
   mal,
   geteilt,
   res
)

# parseInt von string zu number casten
# str() castet von number zu string

xs = [1, 2, 3, 4, 5] # .length

print(
    len( str(10) ),
    len( xs )
)

print(
   "\"Hallo Welt\". Ich bin hier und danke!",
   '\"Hallo Welt\". Ich hier und danke!'
   "'Hallo Welt'. Ich hier und danke!"
)

True and False # && and  || or

if True:
   print("it is true")

# if (false) {
#    console.log()
# } else {
#    console.log()
# }

if False:
    print("is false")
else: 
    print("this is from false")

#true or false

print(
   type([1,2,3,4]),
   type(5),
   type({"name":  "dimi"}), # dict in js obj
   type("string")
)

a = 5
a = 10
a = 15

print(a)

test = 1
Test = 5

# case-sensitive !!!
print(
   test,
   Test
)

ひらがな="Konichiva"
官话="mandarin"

print(
    ひらがな,
    官话
)

print("print my module name", __name__)

# fathersName -> bad JS -> camelCase
# fathers_name -> good Python -> snake case

# class Person: -> python
# class Person() {} -> js
# class BookPublisher -> PascalCase

# const name = "Dimi"
NAME = "Dimi"

a = 1
b = 2
# a , b = 1 , 2

#a, b = 1, 2
#a, b = b, a

print(a, b)

print(
    "Ho!" * 3
)