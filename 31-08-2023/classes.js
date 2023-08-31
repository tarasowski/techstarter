/*
var Car = function() {
    this.mileage = 0
    this.color = "red"
    this.brand = "BMW"
}

Car.prototype.drive = function(km) {
    this.mileage += km
}

Car.prototype.changeColor = function(color) {
    this.color = color
}

Car.prototype.changeBrand = function(brand) {
    this.brand = brand
}
var car = new Car()

car.drive(50)
car.drive(80)
car.changeColor("green")
car.changeBrand("fiat")

console.log(
    "Marke", car.brand,
    "Farbe", car.color
    )

*/

class Car {
    constructor() {
        this.mileage = 0
    }
    drive(km) {
        this.mileage += km 
    }
}

class SuperCar extends Car {
    constructor(ps) {
        super()
        this.ps = ps
    }
    addPs(ps) {
        this.ps += ps
        console.log("🚗 PS added")
    }
}

var ferrari = new SuperCar(500)
ferrari.addPs(500)
console.log(ferrari)




class Truck extends Car {
    constructor(tonnen) {
        super()
        this.totalLoad = 0
        this.maxLoad = tonnen
    }
    load(t) {
        /* hier kommt der Inhalt  */
        console.log("truck wird geladen", t)
    }
    unload(t) {
        /* hier kommt den Inhalt */
        console.log("truck wird entladen", t)
    }
}



let truck = new Truck(7)
truck.drive(150)
truck.load(50)
truck.unload(50)
console.log(truck)


/*
let car = new Car()
car.drive(30)
car.drive(50)
console.log(car.mileage)
*/