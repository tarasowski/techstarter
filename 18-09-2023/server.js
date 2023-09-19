import express from "express"
// express is a constructor
// a constructor creates an object
// an object hast properties (keys/value) and methods (functions)
const app = express()

const port = 3000

let count = 5

const callback = (req, res) => {
    count += 1
    res.json( {message: "hello world", username: "Dimi"} )
    /*
    res.send(`
        <h1>Soll neu dargestellt werden</h1>
        <p>Das ist mein Text welher dargestellt werden soll</p>
        <span>${count}</span>
    `)
    */
}
// app.get("/", callback(req, res))
app.get("/", callback)

class Product {
    constructor(id, name, price, category) {
        this.id = id 
        this.name = name
        this.price = price
        this.category = category
    }
}

let products = []

products.push(new Product(1, "LG TV", 500, "Entertainment"))
products.push(new Product(2, "Panasonic TV", 900, "Entertainment"))
products.push(new Product(3, "iPhone", 1500, "Productivity"))
products.push(new Product(4, "iPhon Plus+++", 5000, "Productivity"))

// /products -> is the route 
app.get("/products", function(req, res) {
    // read the products from db
    // return the products
    res.json(products)
})

let id = 4

app.get("/products/add", function(req, res){
    id += 1
    products.push(new Product(id, "Test Product", 500, "Test Category"))
    res.send("Product added")
})

// "/products/:id" -> **route** is the name for that
app.get("/products/:myId/:myName", function(req, res) {
    const myId = req.params.myId
    const myName = req.params.myName

    const myProduct = products.find(product => product.id === parseInt(myId))
    res.json(myProduct)
})

// function() {} here is a callback
app.listen(port, function() {
    console.log(`Server läuft auf Port ${port}`)
})
