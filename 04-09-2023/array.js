/*

Sie erhalten ein Array von Objekten, die Bücher mit einem Autor und einem Titel darstellen, der wie folgt aussieht:

const books = [
  {
    title: 'Book',
    author: 'Name'
  },
  {
    title: 'Book2',
    author: 'Name2'
  }
]

Ihre Aufgabe besteht darin, eine Funktion zu schreiben, die das Array übernimmt und ein Array von Titeln zurückgibt:

getTheTitles(books) // return ['Book','Book2']

*/

const books = [
  {
    title: 'Book1',
    author: 'Name1'
  },
  {
    title: 'Book2',
    author: 'Name2'
  },
  {
    title: 'Book3',
    author: 'Name3'
  }
]

function getTitles(books) {
    const titles = books.map(book => book.title)
    return titles
}


function removeBook(books, bookToRemove) {
    const filteredBooks = books.filter((book => book.title !== bookToRemove))
    // A FUNCTION SHOULD ALWAYS RETURN
    return filteredBooks
}

console.log(
    //getTitles(books),
    removeBook(books, "Book2") 

)

//Bonus (Russian Roulette Game 😱):

// firePosition ist die Position, in der die Waffe abgefeuert wird.

let firePosition = 1;

// Die Ausgabe von spinChamber ist eine "randome" Zahl und kann als Parameter an die Funktion fireGun übergeben werden.

const spinChamber = () => {
    // ein inverval zwischen 1 - 8
    return Math.floor(Math.random() * 8) + 1
};

// fireGun prüft ob die Zahl aus spinChamber mit der Zahl aus firePosition übereinstimmt, falls JA return "Du bist 🔫" falls NEIN return "Spiel weiter 🎲".

const fireGun = (bulletPosition) => {
 // here is your code
 if (bulletPosition === firePosition) {
    return "Du bist pifpaf 🔫"
 } else {
    return "Spiel weiter"
 }
};

const bulletPosition = spinChamber()
const result = fireGun(bulletPosition)

console.log(
    //fireGun(spinChamber())
    result,
    );