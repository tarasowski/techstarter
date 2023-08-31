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
neuesTierHinzufuegen("Delfin", "Säugetier", 25, "18:00")

tierInformationenAktualisieren("Löwe", 6, "14:00");
tierInformationenAnzeigen();

console.log("Diese Tiere leben im Zoo: ", zooTiere)

// Bonus-Herausforderung: Funktion zum Berechnen der durchschnittlichen Lebensdauer
function durchschnittlicheLebensdauerBerechnen() {
    // Berechne den Durchschnitt der Alter der Tiere
    // Tipp: Verwende Array-Funktionen wie map() und reduce()
}

