import fs from "fs" // file system built-in module
import http from "http" // http module built-in in node

//fs.writeFile() -> async
//fs.writeFileSync("hello.txt", "Hello from Node.js") //--> sync

console.log("wir starten mit dem script")

try {
    //throw new Error("xxxx -> here is the error <-- xxx")
    fs.writeFileSync("hello.txt", "Hello from Node.js") //--> sync
    console.log("file was written to the fs")
} catch(e) {
    console.error("this is an error", e)
}

console.log("wir sind fertig mit dem script")

const listOfUsers = {
    users: [
        {
            id: 1,
            name: "John"
        },
        {
            id: 2,
            name: "Jane"
        }
    ],
    count: 2
}

function test() {
    try {
       const user =  listOfUsers.address.street
       console.log(user)
       return user
    } catch(e) {
        console.error("this is an error", e)
        return undefined
    }
}

test()

console.log("unsere application läuft weiter")