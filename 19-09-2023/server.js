import express from "express"
import bodyParser from "body-parser"
import cors from "cors"
import fs from "fs"


const app = express()
const port = 3000
const fileName = "./todos.json"
const url = "http://localhost:3000/save"

app.use(bodyParser.json());

app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());


//app.use(express.urlencoded({ extended: true }));

// model -> hier werden die Daten für das rendering gespeichert
// 👇 this is the model (MVC - model, view, controller)
let todos = [
    {id: 1, description: "Auto waschen gehen", name: "Dimi"},
    {id: 2, description: "Fahrad fahren gehen", name: "Evelyn"},
    {id: 3, description: "JS Unterlagen vorbereiten", name: "Bartek"}
]


// SSR - server-side rendering
function createForm() {
    return `
<!--  👇 this is our view in the M V C -->
<h1>Meine TodoListe</h1>
<ul>
<li></li>
${todos.map(todo => '<li>' + todo.description + ' • responsible for • ' + todo.name + '</li>').join(" ")}
</ul>
<form action="/add-todo" method="POST">
    <label for="todo">Your todo</label>
    <input name="myTodo" id="todo" type="text" placeholder="Your todo" />
    <label for="firstName">Your Firstname</label>
    <input name="myName" type="text" id="firstName" placeholder="Your firstname" />
    <input type="submit" value="Add todo">
</form>
<button onClick="handleSave()">Speichern</button>

<script>
// 👇 this is our controller in the MVC
const handleSave = async () => {
    try {
        const response = await fetch("${url}")
        alert("Successfully saved")
    } catch(e) {
        alert("There was an issue. Please contact the admin!")
    }
}
</script>
`
}

const json = fs.readFileSync(fileName).toString('utf8') // implicit type conversion stattfinden von json to js object?

if (typeof(json) === "string") {
    const data = JSON.parse(json)
    todos = data
}

// route /
/*
 app.get("/", function(req, res) {

})

app.post("/", function(req, res) {

})

app.post("/add-todo", function(req, res) {

})
*/

app.delete("/delete-order", function(req, res) {
    console.log("print my req", req)
    res.send("Your order has been deleted!")
})

app.post("/order-pizza", function(req, res) {
    const customerName = req.body.name
    //console.log(req.body.name)
    // sends always in text/html format
    //res.send(`Vielen Dank für diese Bestellung: ${customerName}`)
    res.json({message: "Thank you for your order"})
})

app.get("/test", function(req, res) {
    console.log("request infos", req.get("User-Agent"))
    res.send("Hello from the server")
})

app.get("/", function(req, res) {
    res.send(createForm())
})

app.get("/save", function(req, res) {
    console.log("save todo list")
    // damit speicher wir under todos = [] auf der Festplatte
    const data = JSON.stringify(todos)
    fs.writeFileSync(fileName, data)
    res.send("Todo list is saved")
})

app.post("/add-todo", function(req, res) {
    //const { myTodo, myName } = req.body

    // get information from request
    const myTodo = req.body.myTodo
    const myName = req.body.myName
    const nextId = todos.length + 1

    // todo object
    const myNewTodo = {
        id: nextId, 
        description: myTodo,
        name: myName,
    }

    todos.push(myNewTodo)

    //res.send("Form successfully submitted")
    //res.send("Successfully saved")

    // schick antwort an den client
    res.redirect("/")
})


app.listen(port, function() {
    console.log(`Server is online under the port: ${port}`)
})