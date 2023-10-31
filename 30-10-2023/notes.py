color = "blue"

# switch 
if color == "red":
    print("it is true")
    pass
elif color == "green":
    print("my color is green")
    pass
elif color == "blue":
    print("from my blue")
    pass
elif color == "orange":
    print("from my blue")
    pass
elif color == "yellow":
    print("from my blue")
    pass
elif color == "gray":
    print("from my blue")
    pass
else:
    print("coming from else")
    pass

# turnary operator
#true ? "is true" : "is false"

a = "5"

"Ja, 5" if a == 5 else "Nein, keine 5"

if (a == 5):
    print("Ja, 5")
else:
    print("Nein, keine 5")

# try {} catch(e) {}
# try: except:

def read_data():
    try:
        file = open("test.txt", mode= "r")
        return file.read()
        #("print try block")
        #print(file.read())
    except Exception as e: 
        #print("except block")
        #print("comes form exception", e)
        # mode="a" is append
        f = open("test.txt", mode= "w")
        f.write("Now the file has more content!")
        f.close()
        # this runs always 👇

#content = read_data()

#print("content", content)
#print("das Programm läuft weiter !!!")

# `${varName} here is my message`

var_1 = "hello"
var_2 = "world"

print(
    #"{}, {}!".format(var_1, var_2),
    #"{0}, {0}!".format(var_1, var_2), # wir arbeiten hier mit indx
    f"{var_1} hier ist my var_1, {var_2} hier is my var2"
    f"{var_2} hier ist was ich sagen" # syntatic sugar
)

name = "Bartek"

def change_val():
    return "Pablo" 

name = change_val()

print(f"Hallo {name}!")

# Encapsulation -> Class (attribute) + methoden

class Car():
    def __init__(self, color):
        self.color = color
    def change_color(new_color):
        Car.color = new_color

class Greeting():
    def __init__(self, name):
        self.name = name
    def change_name(new_name):
        Greeting.name = new_name
        return f"Hallo {Greeting.name}"

def change_name(new_name):
    return f"Hallo {new_name}"

# var -> kann immer überschrieben werden
# const -> kann nicht überschrieben werden



 
    