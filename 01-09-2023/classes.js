// wir bauen ein online shop
// betreiber kann produkte erstellen
// kunde kann produkte hinzufügen, entfernen etc.
// kunde kann bezahlen

// wir sind JEFF BEZOS

class Product {
    constructor(price, name, id, category) {
        this.price = price
        this.name = name
        this.id = id
        this.category = category
    }
}

let p1 = new Product(1000, "Fernseher", 1, "Entertainment") 

/* 
let p1 = {
    price: 1000,
    name: "Fernseher",
    id: 1,
    category: "Entertainment"
} 
*/

let p2 = new Product(2000, "Macbook Pro", 2, "Computer")

let p3 = new Product(500, "Waschmaschine", 3, "Haushalt")

console.log(
   // p1,
   // p2,
   // p3
)

class ShoppingCart {
    constructor() {
        this.products = []
        this.totalPrice = 0
    }
    // ⬇️ are methods
    addingToCart(product) {
        console.log("Das Produkt wird hinzugefügt: ", product)
        this.products.push(product)
        this.totalPrice += product.price
    }
    deleteFromCart(product) {
        console.log("Das Produkt wird entfernt: ", product)
        this.totalPrice -= product.price
        //this.products = this.products.filter(p => p.id !== product.id)
        let idx = this.products.findIndex(p => p.id === product.id)
        // === equal
        // !== not equal
        if (idx !== -1) {
            this.products.splice(idx, 1)
        }

    }
    printCart() {
        console.log(
            "Here sind alle Produkte aus dem Warenkorb: 💰",
             this.products,
             "Das ist der Endpreis: 💵",
             this.totalPrice
            )
    }
    listProducts(){
                                            // string literals
        return this.products.map(product => `Produktname: ${product.name} - Produktpreis: ${product.price}`)
    }
    // replaceProduct
    // payFinalPrice
}

let cart = new ShoppingCart()

cart.addingToCart(p1)
cart.addingToCart(p2)
cart.addingToCart(p3)
cart.deleteFromCart(p1)

console.log(
    cart.listProducts()
)

// dot notation
//console.log("Preis", cart.totalPrice)
//console.log("Products", cart.products)

// bracket(s) [] notation
console.log("Preis", cart["totalPrice"] )
console.log("Products", cart["products"])



// bracket notation
//cart.printCart()


//console.log(cart)

//const xs = [1, 2, 3, 4, 5]

/*
Schreiben Sie eine Funktion, die die Zeichenfolge einfach eine bestimmte Anzahl von Malen wiederholt:

repeatString('hey', 3) // return 'heyheyhey'
Diese Funktion benötigt zwei Argumente, string und num.
*/

function repeatString(str, n) {
    let result = ""
    for (let i = 1; i <= n; i++) {
        result += str
    }
    return result
}

function repeatString2(str, n) {
    return str.repeat(n)
}

console.log(
    repeatString("hey", 3),
    repeatString2("hey", 3)
)

/*
Schreiben Sie eine Funktion namens „reverseString“, die ihre Eingabe umgekehrt zurückgibt!
reverseString('hello there') // return 'ereht olleh'
*/

function reverseString(str) {
    const chars = str.split("");
    const reverseChars = chars.reverse()
    const reversedString = reverseChars.join("")
    return reversedString
    /*
    return str
            .split("")
            .reverse()
            .join("")
    */
}

function reverString2(str) {
    return [...str].reverse().join("")
}

const reversedString3 = function(str) {
    return str.split("").reverse().join("")
} 

const myString = "Hello World!"
const reversedString = reversedString3(myString)


console.log(
    reverseString("Hello World!"),
    reverString2("Hello World!"),
    [..."Hello World"].reverse().join(""),
    reversedString
)

/*
Schreiben Sie zwei Funktionen, 
die Temperaturen von Fahrenheit in Celsius und umgekehrt umrechnen:
convertToCelsius(32) // return 0 convertToFahrenheit(0) // return 32
*/
