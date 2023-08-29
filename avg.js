/* 

Schreibe eine JavaScript-Funktion, die den Durchschnitt von einer Liste von Zahlen berechnet. 
Erstelle dann eine Beispielliste von Zahlen und verwende die Funktion, um den Durchschnitt dieser Zahlen zu berechnen.

*/

// function avg, var arr, var res

function average(numbers) {
    let sum = 0;
    for (let number of numbers) {
        sum += number;
    }
    return sum / numbers.length
}

let numbers = [1,2,3,4,5]

let result = average(numbers)
//console.log("Dennis ", result)
function avg2(numbers) {
    return numbers.reduce(
        // lambda function
        (acc, number) => acc + number

        , 0) / numbers.length
}
// map creates a new array
function addFive(n) {
    //console.log("element", n)
    return n + 5
}

let xs = [1,2,3,4,5]

let res3 = xs.map(addFive) // higher order functions

function biggerThan3(n) {
    console.log("this is the number: ", n)
    console.log("this is the return value: ", n > 3)
    return n > 3
}

let res4 = xs.filter(biggerThan3)

function makeSum(acc, num) {
    // let xs = [1,2,3,4,5]
    // 1 iteration acc = 0, num = 1
    // return 0 + 1 = 1
    // 2 iteratio acc = 1, num = 2
    // return 1 + 2 = 3 
    // 3 iteration ....
    return acc + num

}

let res5 = xs.reduce(makeSum, 0)

console.log(res5)

/*
    [].map()
    [].filter()
    [].reduce()
*/



/* always the fame function

const fnName = (acc, number) => { 
    return acc + number 
}

const fnName = (acc, number) => ( acc + number )


function fnName(acc, number) {
    return acc + number 
} 

const fnName = function(acc, number) {
    return acc + number 
}

*/


let res2 = avg2(numbers)
//console.log("Enrico: ", res2)