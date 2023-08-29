/* Erstelle ein JavaScript-Programm, 
das den Benutzer nach seinem Namen fragt 
und dann eine personalisierte 
Begrüßungsnachricht ausgibt.
*/

// decomposition

// mock data
//let name = ""
//let input = ""
//let result = "Hello " + name

import * as readline from 'node:readline/promises';
import { stdin as input, stdout as output } from 'node:process';

const rl = readline.createInterface({ input, output });

const answer = await rl.question('What is your name? ');

console.log(`Hey 👋 ${answer}`);

rl.close();

function greeting(name) {
    return "Hey 👋 " + name
}

//const result = greeting("Pablo")
//console.log(result)