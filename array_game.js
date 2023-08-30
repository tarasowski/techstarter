/*
In dieser Aufgabe wirst du ein textbasiertes Fantasy-Abenteuer erstellen, bei dem du map, filter und reduce verwenden musst, 
um verschiedene Situationen und Entscheidungen im Spiel zu verwalten. 
Der Spieler wird vor Entscheidungen gestellt, die das Spiel beeinflussen, 
und am Ende wird basierend auf den getroffenen Entscheidungen das Ergebnis ermittelt.
*/

/*
1. Erstelle ein Array von Szenarienobjekten, jedes mit einem Text für die Situation, möglichen Entscheidungen und den Konsequenzen dieser Entscheidungen.
2. Verwende map, um das Array von Szenarienobjekten in eine Liste von Situationen umzuwandeln, die dem Spieler angezeigt werden.
3. Biete dem Spieler die Möglichkeit, eine Entscheidung für jede Situation zu treffen, indem er die Nummer der gewünschten Option eingibt.
4. Verwende filter, um basierend auf den getroffenen Entscheidungen die relevanten Konsequenzen zu filtern.
5. Verwende reduce, um die gesammelten Konsequenzen zu verarbeiten und das Endresultat zu ermitteln.
6. Gib am Ende das Ergebnis des Abenteuers basierend auf den getroffenen Entscheidungen aus.
*/

const scenarios = [
    {
        situation: "Du stehst vor einer mysteriösen Höhle. Was möchtest du tun?",
        choices: ["Betrete die Höhle.", "Gehe zurück in die Stadt."],
        consequences: [
            "In der Höhle findest du einen versteckten Schatz! Du kehrst als Held in die Stadt zurück.",
            "Du kehrst in die Stadt zurück und verpasst die Chance auf den Schatz."
        ]
    },
    {
        situation: "Du triffst auf einen alten Mann, der um Hilfe bittet. Was tust du?",
        choices: ["Hilf dem alten Mann.", "Ignoriere den alten Mann."],
        consequences: [
            "Du hilfst dem alten Mann und er schenkt dir eine magische Karte.",
            "Du ignorierst den alten Mann und setzt dein Abenteuer fort."
        ]
    },
    {
        situation: "Du trifft auf ein wildes Pokemon",
        choices: ["Du versuchst das Glumanda zu fangen", "Du rennst weg"],
        consequences: [
            "Du wirst einer der besten Glumanda Trainer der Welt",
            "Garry wird immer besser sein als Du"
        ]
    }
];


let playerDecisions = () => {}
let adventureResult = () => {} 

console.log("Abenteuer beendet. Ergebnis:");
console.log(adventureResult);

/*
const playerDecisions = scenarios.map((scenario) => {
    console.log(scenario.situation);
    scenario.choices.forEach((choice, index) => {
        console.log(`${index + 1}. ${choice}`);
    });
    const decision = parseInt(prompt("Deine Entscheidung:")) - 1;
    return scenario.consequences[decision];
});

const adventureResult = playerDecisions.reduce((result, consequence) => {
    return result + " " + consequence;
}, "");

*/
