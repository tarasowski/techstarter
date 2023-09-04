/*
Schreiben Sie zwei Funktionen, die Temperaturen von Fahrenheit in Celsius und umgekehrt umrechnen:

convertToCelsius(32) // return 0 convertToFahrenheit(0) // return 32
*/

// es6 import
import { read } from "fs"
import * as readline from "readline"

// require variant
// const readline = require("readline")

function convertToCelsius(fahrenheit) {
    return (fahrenheit - 32) / 1.8
}

function convertToFahrenheit(celsius) {
    return (celsius * 1.8) + 32
}
// rl is the instance of class readlin            // class readline
const rl = readline.createInterface({input: process.stdin, output: process.stdout})

// rl.question("hier kommt was rein", callback) -> this is a callback function
rl.question("Gebe die in fahrenheit ein: ", (fahrenheit) => {
    const converted = convertToCelsius(fahrenheit)
    console.log(converted)
    rl.close()
})



/*
console.log(
    convertToCelsius(32), // -> return 0
    convertToFahrenheit(0) // -> return 32 
)
*/



//prompt("gebe die zahl in fahrenheit ein: ")