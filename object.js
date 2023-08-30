/* 
Aufgabe: Objekt-Abenteuer

Deine Aufgabe besteht darin, ein einfaches JavaScript-Programm zu 
erstellen, das ein Abenteuer in einem Objekt darstellt. 
Du hast ein Objekt namens abenteuer, das Informationen über verschiedene 
Stationen eines Abenteuers enthält. 
Jede Station wird durch einen Namen und eine Beschreibung repräsentiert.

*/

const abenteuer = {
    start: "Du stehst am Anfang deines Abenteuers.",
    wald: "Du betrittst einen dunklen Wald voller Geheimnisse.",
    fluss: "Du kommst an einen reißenden Fluss, der deinen Weg blockiert.",
    hoehle: "In der Höhle leuchten seltsame Kristalle in allen Farben.",
    berge: "Du befindest dich in den Bergen und suchst nach einem Schatz",
    schatz: "Du findest einen versteckten Schatz und spürst, dass dein Abenteuer erfolgreich war!",
    //  done Füge hier weitere Stationen hinzu, wenn du möchtest.
  };
  
// TODO: Schreibe den Code hier, um das Abenteuer zu durchlaufen und die Beschreibungen auszugeben.

function stations(obj) {
  for (let station in obj) {
    if (obj.hasOwnProperty(station)) {
      console.log(`${obj[station]}`)
    }
  }
}

const res = stations(abenteuer)

//console.log(res)

const res2 = Object.keys(abenteuer)
                   .forEach(station => console.log(`${station}::: ${abenteuer[station]}`))



for (let station in abenteuer) {
  console.log(station + "." + abenteuer[station]);
}



function startAdventure() {
  let currentStation = "start"
  while(currentStation !== "schatz") {
    console.log(abenteuer[currentStation])
  }
}

// 1 step: Object.key(adventure) -> man erstellt ein array ["start", "wald"...]

// 2 step: die Schleife iteriert über das neu erstellte array ["start", "wald", ... ]
/*
for (let station of ["start", "wald", ...]) {

}
*/

for (let station of Object.keys(abenteuer)) {
    console.log(`${station}!!! ${abenteuer[station]}`)
}

// in bei objekten
for (let station in abenteuer) {
  console.log(station)
}

// array iteration and not object
for (let i = 0; i < abenteuer.length; i++) {
  console.log(abenteuer[i])
}


// my example
/*
const x = Object.keys(abenteuer)
                .map(station => abenteuer[station])
*/

  