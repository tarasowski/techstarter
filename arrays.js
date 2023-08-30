// Beispiel-Array von Büchern
const books = [
    { title: "Harry Potter", author: "J.K. Rowling", pages: 336 },
    { title: "The Great Gatsby", author: "F. Scott Fitzgerald", pages: 180 },
    { title: "To Kill a Mockingbird", author: "Harper Lee", pages: 281 },
    { title: "1984", author: "George Orwell", pages: 328 },
    { title: "Animal Farm", author: "George Orwell", pages: 500 },
    { title: "Pride and Prejudice", author: "Jane Austen", pages: 432 },
  ];
  
  // Funktion, um die Anzahl der Bücher im Array zu zählen
  function countBooks(books) {
    // pure function no side effects
    return books.length
  }
  
  // Funktion, um alle Buchtitel im Array zurückzugeben
  function getBookTitles(books) {
    let titles = [];
    // []
    // ["title1"]
    // ["titel1", "titel2"]
    // ["titel1", "titel2", "title3h"]

    for (const book of books) {
        titles.push(book.title);
    }
    //return titles; 
    return books.map(
        book => book.title
        )
  }
  
  // Funktion, um Bücher eines bestimmten Autors zurückzugeben
  function getBooksByAuthor(books, author) {
    // filter returns either true or false
    // books -> [{..}, {...}, {...}]
    // filter -> [{...}] 
    // map -> ['1984']
    // [0] -> '1984'
    return books.filter(book => book.author === author)
                .map(book => book.title)
                .join(",")
  }
  
  // Funktion, um die durchschnittliche Anzahl der Seiten aller Bücher zu berechnen
  function averagePageCount(books) {
    // reduce methode
    // gesamtzahl der seiten 
    // durchscnitt 
    // durschnitt runden

    // 1st iteration: acc = 0 book.pages = 336
    // 2nd iteration: acc = 0 + 336 book.pages = 180
    // 3rd iteration: acc = 336 + 180 book.pages = 281
    let totalPageCount = books.reduce((acc, book) => acc + book.pages, 0) 
    // let totalPageCount = books.reduce((acc, book) => acc + book.pages, 0) / books.length
    // Math.round(totalPageCount)

    //return Math.round(books.reduce((acc, book) => acc + book.pages, 0) / books.length)

    // let totalPageCount = books.reduce((acc, book) => acc + book.pages, 0) / books.length
    return Math.round(totalPageCount / books.length)
  }
  
  console.log("Anzahl der Bücher:", countBooks(books));
  console.log("Buchtitel:", getBookTitles(books));
  console.log("Bücher von GO:", getBooksByAuthor(books, "George Orwell"));
  console.log("Durchschnittliche Seitenzahl:", averagePageCount(books));
  