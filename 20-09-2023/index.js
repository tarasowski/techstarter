import express from "express"
const app = express()

const port = 3000

const myMiddleware = (req, res, next) => {
    console.log("This is the middleware");
    next(); // Call next to move on to the next middleware or route handler
  };

//app.use(myMiddleware)
//app.use(express.json)

app.get("/", function(req, res) {
    res.send("Hello world")
})

app.listen(port, function() {
    console.log("Sever läuft auf Port:" + port)
})

