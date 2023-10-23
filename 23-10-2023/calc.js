// TDD - test driven development / XP
// hier wird zuerst ein Test geschreiben


function add(num1, num2) {
    return num1 + num2
}

function test(actual, expected) {
    return actual === expected ? "Der Test ist erfolgreich" : "Der Test ist nicht efolgreich"
}

console.log(
    test( add(1, 2), 3 )
)