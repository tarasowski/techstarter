const arr = Array.apply(0, {length: 100})

function applyToArray(elem, index, arr) {
    return index
}

//applyToArray(undefined, 0, ".....")

const arrModifed = arr.map(applyToArray)

//console.log(arrModifed)

function countFitsNumber(divisor) { 
    const nummer = 2; 
    let i = 0; 
    let tempNumber = divisor; 
    while (tempNumber >= nummer) {
        tempNumber -= nummer;
        i++;
    } 
    console.log("Die zahl 2" + i + ".....")
    return i 
}

let inputDivisor = 23

console.log(
    "Die zahl 2 passt: " + countFitsNumber(inputDivisor) + "mal in " + inputDivisor 
    )

