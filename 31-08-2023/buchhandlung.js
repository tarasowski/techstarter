// Array von Büchern mit Titel, Autor, Genre und Bewertung
const buecher = [
    { titel: "Buch A", autor: "Autor 1", genre: "Fantasy", bewertung: 4.5 },
    { titel: "Buch B", autor: "Autor 2", genre: "Science Fiction", bewertung: 3.8 },
    { titel: "Buch C", autor: "Autor 3", genre: "Fantasy", bewertung: 4.2 },
    { titel: "Buch D", autor: "Autor 4", genre: "Mystery", bewertung: 4.8 },
    { titel: "Buch E", autor: "Autor 5", genre: "Science Fiction", bewertung: 3.5 }
];

// Schritt 2: Verwende map, um eine Liste der Buchtitel zu erstellen
const getTitle = (bucher) =>  {
    return bucher.titel
}
const titelListe = buecher.map(getTitle) 
console.log("Liste der Buchtitel:", titelListe);

// Schritt 3: Verwende filter, um eine Liste von Büchern im Genre "Fantasy" zu erstellen
const fantasyBuecher = buecher.filter((buch) => buch.genre === "Fantasy")
console.log("Fantasy Bücher:", fantasyBuecher);

// Schritt 4: Verwende filter, um eine Liste von Büchern mit Bewertung 4.0 oder höher zu erstellen
const hochBewerteteBuecher = buecher.filter((buch) => buch.bewertung >= 4.0 )
console.log("Hoch bewertete Bücher:", hochBewerteteBuecher);

