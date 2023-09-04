/*
Als stolzer Besitzer eines virtuellen Zoos bist du dafür verantwortlich, 
Informationen über die Tiere in deinem Zoo zu verwalten. 
Deine Aufgabe ist es, ein einfaches Tierverwaltungssystem zu erstellen, 
das es dir ermöglicht, Tierinformationen hinzuzufügen, zu aktualisieren, anzuzeigen und zu löschen.
*/

// Schritt 1: Erstelle ein leeres Array für die Zoo-Tiere
const zooTiere = [];

// Schritt 2: Funktion zum Hinzufügen eines neuen Tieres
function neuesTierHinzufuegen(nName, nArt, nAlter, nFuetterungszeit) {
    const tier = {
        name: nName,
        art: nArt,
        alter: nAlter,
        fuetterungszeit: nFuetterungszeit
    }

    zooTiere.push(tier)
}

// Schritt 3: Funktion zum Aktualisieren von Tierinformationen
function tierInformationenAktualisieren(name, neuesAlter, neueFuetterungszeit) {

}

// Schritt 4: Funktion zum Anzeigen von Tierinformationen
function tierInformationenAnzeigen() {

}

// Schritt 5: Funktion zum Entfernen eines Tieres
function tierEntfernen(name) {
    // Finde das Tier im Array und entferne es
    // Tipp: Verwende Array-Funktionen wie findIndex() und splice()
}

// Schritt 6: Hier rufe die Funktionen auf, um den Ablauf zu testen

// Beispielaufrufe:
neuesTierHinzufuegen("Löwe", "Säugetier", 5, "12:00");
neuesTierHinzufuegen("Giraffe", "Säugetier", 8, "10:00");

tierInformationenAktualisieren("Löwe", 6, "14:00");
tierInformationenAnzeigen();

console.log("Diese Tiere leben im Zoo: ", zooTiere)

// Bonus-Herausforderung: Funktion zum Berechnen der durchschnittlichen Lebensdauer
function durchschnittlicheLebensdauerBerechnen() {
    // Berechne den Durchschnitt der Alter der Tiere
    // Tipp: Verwende Array-Funktionen wie map() und reduce()
}

const customer = {
    id: 1,
    name: "Bartek",
    // traverse
    address: {
        street: "Berliner str",
        homeNumber: 39,
    },
    lastOrderIds: [1, 2, 3, 4, 5]
}

let a = "Hello World"
let b = "Caio World"

let x = 1
let y = "1" // -> 1

let n = 5
let nn = 10

/*
console.log(
    // dot notation
    customer.name,
    // [] notation
    customer["name"],
    customer.address, // undefined
    customer.address.street,
    customer.address.postalCode, // -> undefined
    a === b, // -> false 
    a !== b, // -> true
    x == y, // implicit type conversion
    x === y,
    n < 10,
    n > 10,
    n < nn
)

*/


function greetings(firstName, lastName) {
    // your code
    //console.log("Hallo, " + firstName + lastName + ", schoen dass du da bist!")
    // a function should always return a value either (number, string or object or an array or a boolean)
    //const x = `Hallo, ${firstName} ${lastName}, schoen dass du da bist!`
    //return x
    return `Hallo, ${firstName} ${lastName}, schoen dass du da bist!`
} 

// implicit return statement is added automatically 
let greetings2 = (firstName, lastName) => `Hallo, ${firstName} ${lastName}, schoen dass du da bist!`

let greetings3 = (firstName, lastName) => {
    // explicit return statement here
    return `Hallo, ${firstName} ${lastName}, schoen dass du da bist!`
}

const res = greetings("Christoph", "Raupach")

const res2 = greetings2("Enrico", "C")

console.log(
    res,
    res2
)




