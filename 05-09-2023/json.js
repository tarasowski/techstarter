import fs from "fs"

/*
const customer = {
    name: "Pablo",
    id: 1,
    address: "Berlinerweg",
    interests: ["coding", "cooking"]
}

const objectAsJson = JSON.stringify(customer)

fs.writeFileSync("./customers.json", objectAsJson, "utf-8")
*/

/*
let customer = {}

const rawData = fs.readFileSync("./customers.json")
const parsed = JSON.parse(rawData)
customer = parsed

delete customer.id


console.log(
    //JSON.parse(x),
    customer
    )

//console.log(JSON.stringify(customer))
*/

console.log("1 step: unser program wird gestartet")

// asynchronon
fs.readFile("./customers.json", (data) => {
    console.log("2 step: die daten werden bearbeitet")
})

console.log("3 step: unser program wird beendet")