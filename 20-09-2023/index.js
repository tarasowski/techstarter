import express from "express"
const app = express()

const port = 3000

app.get("/", function(req, res) {
    res.send("Hello world")
})

app.listen(port, function() {
    console.log("Sever läuft auf Port:" + port)
})

