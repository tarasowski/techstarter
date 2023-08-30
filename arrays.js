// Beispiel-Array von Büchern
const books = [
    { title: "Harry Potter", author: "J.K. Rowling", pages: 336 },
    { title: "The Great Gatsby", author: "F. Scott Fitzgerald", pages: 180 },
    { title: "To Kill a Mockingbird", author: "Harper Lee", pages: 281 },
    { title: "1984", author: "George Orwell", pages: 328 },
    { title: "Pride and Prejudice", author: "Jane Austen", pages: 432 },
  ];
  
  // Funktion, um die Anzahl der Bücher im Array zu zählen
  function countBooks(books) {
    let count = books.length
    console.log(count)
    return 
  }
  
  // Funktion, um alle Buchtitel im Array zurückzugeben
  function getBookTitles(books) {
  }
  
  // Funktion, um Bücher eines bestimmten Autors zurückzugeben
  function getBooksByAuthor(books, author) {
  }
  
  // Funktion, um die durchschnittliche Anzahl der Seiten aller Bücher zu berechnen
  function averagePageCount(books) {
  }
  
  console.log("Anzahl der Bücher:", countBooks(books));
  console.log("Buchtitel:", getBookTitles(books));
  console.log("Bücher von J.K. Rowling:", getBooksByAuthor(books, "J.K. Rowling"));
  console.log("Durchschnittliche Seitenzahl:", averagePageCount(books));
  