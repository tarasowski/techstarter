/* 
Erstelle ein JavaScript-Programm, 
das den Benutzer nach zwei Zahlen fragt und 
dann die Summe, Differenz, Produkt und Quotient der beiden Zahlen ausgibt.
*/

// var a, b 
// dennis
let a
let b

function isNumber(x) {
    //if (typeof(x) === 'number')
    if (!isNaN(x)) {
        return x
    } else {
        return prompt("bitte gebe gültige zahl ein: ")
    }
}

console.log("bitte geben sie mir die erste zahl ein")
a = isNumber( parseInt( prompt("erste zahl") ) )

console.log("bitte geben sie mir die zweite zahl ein")
b = isNumber(  parseInt( prompt("zweite zahl") ) )


const sum = (a, b) => {
    return a + b
}

function checkIfNumber(x) {
   if (!isNaN(a) && !isNaN(b)) {
    return [sum(a, b), product(a, b), diff(a, b), quot(a, b)]
   } else {
    alert("bitte geben sie eine gültige zahl ein!")
    return null
   } 
}

checkIfNumber(a, b)



function diff(a, b) {
    return a - b
}

function product(a, b) {
    return a * b
}

function quot(a, b) {
    return a / b
}

document.write(`
    <p>Summe: ${sum}</p>
    <p>Difference: ${diff}</p>
    <p>Product: ${product}</p>
    <p>Quot: ${quot}</p>
`)

// bartek
//var a = parseInt(prompt("bitte geben sie mir die erste zahl ein"))
//var b = parseInt(prompt("bitte geben sie mir die zweite zahl ein"))


