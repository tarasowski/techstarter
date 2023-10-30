notes = [4, 5, 1, 1, 5, 6]

for note in notes:
    if note > 4:
        print("Du bist echt schlecht from my for loop")

# [ausdruck for element in liste]

# similar to a map function in JS, wobei python has its own map function !!!
# list comprehension

def add_five(note):
    return note + 5

res = [add_five(note) for note in notes if note > 4]
# () => {}
# lambda x: x + 5
# res2 = [lambda note: note + 5 for note in notes if note > 4]

print(res)


# list comprehension the expression should always return
xs = [1, 2, 3]

def add_five(num):
    print(num + 5)
    return num + 5
    
#resxs = [add_five(num) for num in xs]
resxs = [(num + 5) for num in xs]
# [expression for element in range/list ]

print(resxs)

    