const assert = require('assert');

// 1. **Überprüfe, ob zwei Zahlen gleich sind:**

function areEqual(num1, num2) {
  return num1 === num2; // -> return is true or false
}


//assert.strictEqual(areEqual(3, 3), true); // Dieser Test wird bestehen
//assert.strictEqual(areEqual(2, 4), false); // Dieser Test wird bestehen
assert.strictEqual(3, 2)

/*

//2. **Prüfe, ob ein Array sortiert ist:**

function isSorted(arr) {
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[i - 1]) {
      return false;
    }
  }
  return true;
}

assert.strictEqual(isSorted([1, 2, 3, 4]), true); // Dieser Test wird bestehen
assert.strictEqual(isSorted([4, 3, 2, 1]), false); // Dieser Test wird bestehen

//3. **Teste, ob eine Funktion die richtige Ausgabe zurückgibt:**

function add(a, b) {
  return a + b;
}


assert.strictEqual(add(2, 3), 5); // Dieser Test wird bestehen
assert.strictEqual(add(10, 7), 17); // Dieser Test wird bestehen
*/