//import fs from "fs"
import * as fs from 'node:fs/promises'
console.log("1.step: wir starten mit dem script")

/*
fs.writeFile("hello.txt", "Hello from Node.js", function(err) {
    console.log("2.step: the file was created successfully")
    if(err) {
        console.error("this is an error", err)
    } else {
        console.log("file was written to the fs")
    }
})
*/

const asyncWrite = async () => {
    await fs.writeFile("hello.txt", "Hello from Node.js")
    console.log("is ready")
}

console.log("3.step: wir enden mit dem script")

asyncWrite()