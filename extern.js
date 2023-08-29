// Seite 1203

let test = "hello " + "world"
console.log(test)
console.log(typeof(test))

// (param1, param2)

function helloWorld(param1 = 1,param2 = 2, param3 = 3) {
    console.log("param1", param1)
    console.log("param2", param2)
    console.log("param3", param3)
    // there is no return statement
}

const roundToNext10 = (n, n2, n3) => Math.round(n / 10) * 10 


const nameGenerator = (firstName, lastName) => {
    return firstName + " " + lastName
}

const addGreetings = (name) => {
    return "Hello " + name + "!"
}

const name = nameGenerator("John", "Doe")
const greeting = addGreetings(name)

// ternery operator

//const result1 = nameGenerator("John", "Doe") 

//const result3 = addGreetings(result1)

// a function should only do one thing
// a function should be as small as possible

const program = (a, b) => {
    return (a > b) ? "ist grösser" : "ist nicht größer"
}

const makeSquare = (n) => { 
    return n * n
}

let numbers = [1, 2, 3, 4, 5]

// Seite 1216
let squares = numbers.map(
        (elem) => makeSquare(elem)
    )

console.log(squares)





const str = "Hello World"

str.split("").reverse().join("")

str.split(" ")
   .reverse()
   .join(" ")




