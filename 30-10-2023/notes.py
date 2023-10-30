tuple1 = (1, 2)
first, second  = tuple1

# const [first, second] = [1, 2]

print(first, second)

def main(data):
    first, second = data
    return (10, second + 10)

first_from_fn, second_from_fn = main(tuple1)
print(first_from_fn, second_from_fn)

# list is a mutable data structure
xs = [1,2,3,4]
xs[1] = 100

#txs = (1, 2, 3, 4)
#txs[1] = 100
#print(xs)

first_value = (1) # -> integer
first_value_tuple = (1,) #-> tuple

print(type(first_value))
print(type(first_value_tuple))

print( 
    (1, 2, 3) + (4, 5, 6)
)

dct = {"key": "value"}
st = {"value", "value2"}
primes = {2, 3, 5, 7, 11, 13, 17, 19}

set1 = {} # -> dict
set1 = set() # -> set
#empty_tuple = ()
empty_tuple = tuple()

print(
    11 in primes,
    15 in primes,
    9 not in primes,
    7 not in primes,
    {1, 1, 2, 2, 3, 3},
    (1, 2) == (2, 1), # -> False
    [1, 2] == [2, 1], # -> False
    set([1, 2, 2, 2, 1, 1]) == set([2, 1]), # -> True
    sorted([1, 2]) == sorted([2, 1]), # -> True
    type(())
)

# dict
user = {
    "age": 39,
    "name": "John",
}

# bracket notation in JS and dot notation in JS both workd
print(
    #user["ageX"], # -> bracket notation
    user.get("ageX", 0)
)

# check if user is over 18

if user.get("agex", 0) > 18:
    print("User is over 18")
else: 
    print("User is under 18")

# there should not be more than a single if statemetn
# clean code ☝️

def check_if_john(user):
    if user["name"] == "John":
        print("John you hit the jackpot")
        return True
    else: 
        return False

def check_age(user):
    if ("age" in user):
        if user["age"] > 18:
            print("User is over 18")
            check_if_john(user)
        else:
            print("User is under 18")
    else:
        print("User is under 18")


#check_age(user)

weekdays = {"Mo": "Monday", "Tu": "Tuesday", "We": "Wednesday", "Th": "Thursday", "Fr": "Friday", "Sa": "Saturday", "Su": "Sunday"} 

user["address"] = "123 Main St"
#user.address = "123 Main St"

print(
    #weekdays["Mo"],
    weekdays.get("Mo"),
    [day for day in weekdays.values()],
    [day + "!" for day in weekdays.keys()],
    user.get("age") is None, # None is similar to undefined
    user
)

text = "Dies ist ein Test-String"
# shift + =
print(
    text[5]
)

# str = string
# x = unbekannte Zahl
# xs = liste
# obj = object
# range(start, end - 1)
# range(m, n-1)
                #m, n-1
print(list(range(1, 5)))

print(list(range(0, 101)))
print(list(range(10))) # we remove the start value of zero, pythonic way

test = [entry for entry in list(range(0, 101))]




