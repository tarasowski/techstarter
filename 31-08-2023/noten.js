/*
**Aufgabe:**
Du möchtest ein einfaches Programm schreiben, das dir hilft, den Durchschnitt von Noten zu berechnen. Deine Aufgabe ist es, ein Array von Noten zu erstellen und dann den Durchschnitt dieser Noten zu berechnen.

**Schritte:**

1. Erstelle ein Array namens `noten` mit verschiedenen Noten (zum Beispiel 80, 90, 75, 60 usw.).

2. Verwende eine `for`-Schleife, um durch das `noten`-Array zu iterieren und die Summe der Noten zu berechnen.

3. Berechne den Durchschnitt, indem du die Summe der Noten durch die Anzahl der Noten im Array teilst.

4. Gib abschließend den Durchschnitt aus.

**Bonus-Herausforderung:**
Füge eine Bedingung hinzu, die sicherstellt, dass die Noten im gültigen Bereich (zum Beispiel 0-100) liegen.

*/

const noten = [80, 90, 75, 60, 95, 85];

let summe = 0;

// for loop die zur Summe festhaelt
for (let i = 0; i < noten.length; i++) {
    // gültier bereich zwischen 80 <> 90
    // falls nicht im bereich sollte nicht zur Summe addiert werden
    const note = noten[i]
    // check if valid  
    if(note >= 80 && note <= 90) {
        summe += note
    }
}

/*
for (let note of noten) {
    // Bonus: Überprüfe, ob die Note im gültigen Bereich liegt
}
*/

const durchschnitt = summe / noten.length;
console.log(`Durchschnitt: ${durchschnitt.toFixed(0)}`);

