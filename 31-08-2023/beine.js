/*
Du bist ein angehender Tierforscher und möchtest die Anzahl der Beine in verschiedenen Tierarten erforschen. 
Deine Aufgabe ist es, ein einfaches Programm zu schreiben, das dir hilft, die Anzahl der Beine für verschiedene Tiere zu berechnen 
und anzuzeigen.
*/
                    // idx = 0 // idx = 1 ...
const tierarten = ["elefant", "hund", "spinne", "pferd"];

const beineAnzahl = {}

// 1. Aufgabe: Anzahl der Beine für jedes Tier hinzufügen
/*
const elefant = 4
const hund = 4
const spinne = 8
const pferd = 4
*/

/*
beineAnzahl = {
    elefant,
    hund,
    spinne,
    pferd
}

// bracket notation
beineAnzahl["elefant"] = 4
beineAnzahl["hund"] = 4
beineAnzahl["spinne"] = 8
beineAnzahl["pferd"] = 4

*/

// dot notation
beineAnzahl.elefant = 4
beineAnzahl.hund = 4
beineAnzahl.spinne = 8
beineAnzahl.pferd = 4
beineAnzahl.fisch = 0
beineAnzahl.thousandfuessler = 1000

//console.log(beineAnzahl)


// 2. Aufgabe: Beine Anzahl pro Tier ausgeben

for (let i = 0; i > tierarten.length; i++) {
    const tier = tierarten[i] // -> elefant
    const anzahl = beineAnzahl[tier] // -> beineAnzahl["elefant"]
    //console.log(`Das Tier ${tier} hat ${anzahl} Beine`)
}
                 // []
for (let tier of tierarten ) {
    const anzahl = beineAnzahl[tier]
    //console.log(`Das Tier ${tier} hat ${anzahl} Beine`)
}

//const beineAnzahl = {elefant: 4, hund: 4, spinne: 8, pferd: 4};
for (const tier in beineAnzahl) {
    //console.log(`Ein ${tier} hat ${beineAnzahl[tier]} Beine.`)
}

// 3. Aufgabe: Die Azahl der Beine für ein bestimmtes Tier z.B. ein Elefant ausgeben


const tier = "Elefant"

for (const tier in beineAnzahl) {
    //console.log(`Ein ${tier} hat ${beineAnzahl[tier]} Beine.`)
}

function beineAusgabe(tier) {
    const beine = beineAnzahl[tier]
    // wann wird beine = undefined 
    if (beine === undefined) {
        console.log("Tier nicht gefunden")
        return undefined
    } else {
        return beine
    }
}

console.log(
    // function signature
    beineAusgabe("katze"),
    beineAusgabe("hund")
)

