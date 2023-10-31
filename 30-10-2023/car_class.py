class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        # no return 

    def __str__(self):
        return f"Automarke: {self.make}, Automodell: {self.model}, Baujahr: {self.year}, Kilometerstand: {self.speed}"

    def accelerate(self, speed_increase):
        self.speed += speed_increase
        # no return

    def brake(self, speed_decrease):
        self.speed -= speed_decrease
        # no return

    def honk(self):
	# hupen
        print(f"{self.year} {self.make} {self.model} says Honk!")
        # no return

    def display_speed(self):
        print(f"Current speed: {self.speed} mph")
        # no return

# This is the base "Car" class.

# 👇 instance
#car_mercedes = Car("Mercedes", "C-Klasse", 2023)

"""
car_mercedes.accelerate(150)
car_mercedes.brake(50)
car_mercedes.display_speed()
#print("car_mercedes", car_mercedes)
"""

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
	#We provide an __init__ method that calls the parent class's __init__ method using super(). 
	#This initializes the common attributes from the "Car" class and adds the "battery_capacity" attribute for electric cars.
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f"This is my current battery capacity {self.battery_capacity} for {self.make} of model {self.model}"

    def discharge_battery(self, new_battery_capacity):
        print(f"Discharging the battery of the {self.year} {self.make} {self.model}...")
        self.battery_capacity -= new_battery_capacity 

    def charge_battery(self, new_battery_capacity):
        print(f"Charging the battery of the {self.year} {self.make} {self.model}...")
        self.battery_capacity += new_battery_capacity 

    # You can add additional methods or attributes specific to electric cars here.

# Create a regular car
"""
my_car = Car("Toyota", "Camry", 2022)
my_car.accelerate(30)
my_car.display_speed()
my_car.honk()
"""

# this is a constructor function - a constructor creates an object
def create_car(make, model, year):
    return {"make": make, "model": model, "year":  year, "speed": 0}

def change_speed(car, speed):
    return {**car, "speed": speed}

car_mercedes = create_car("Mercedes", "C-Klasse", 2023)
new_speed = change_speed(car_mercedes, 50)



print(
    f"original object: {car_mercedes}", 
    f"new object with new speed {new_speed}"
)

# Create an electric car
"""
my_electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
my_electric_car.accelerate(50)
my_electric_car.display_speed()
my_electric_car.discharge_battery(70)
my_electric_car.charge_battery(50)

print(my_electric_car)
"""

# this is a functional programming approach
"""
def func_1(text):
    print("func_1")
    return text + "."

def func_2(text):
    print("func_2")
    return text + "!!"

def func_3(text):
    print("func_3")
    return text + "???"

text = "das ist mein starting point"
return_func1 = func_1(text)
return_func2 = func_2(return_func1)
return_func3 = func_3(return_func2)

print(return_func3)

output = pipeline(
    func_1,
    func_2,
    func_3
)
"""