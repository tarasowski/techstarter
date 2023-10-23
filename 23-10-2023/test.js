const { areEqual } = require('./yourFile'); // Stellen Sie sicher, dass Sie den richtigen Pfad zur Datei angeben

test('areEqual: 3 should be equal to 3', () => {
  expect(areEqual(3, 3)).toBe(true);
});

test('areEqual: 2 should not be equal to 4', () => {
  expect(areEqual(2, 4)).toBe(false);
});

const { isSorted } = require('./yourFile'); // Stellen Sie sicher, dass Sie den richtigen Pfad zur Datei angeben

test('isSorted: [1, 2, 3, 4] should be sorted', () => {
  expect(isSorted([1, 2, 3, 4])).toBe(true);
});

test('isSorted: [4, 3, 2, 1] should not be sorted', () => {
  expect(isSorted([4, 3, 2, 1])).toBe(false);
});

const { add } = require('./yourFile'); // Replace 'yourFile' with the correct path to your file

test('add: should return the sum of two numbers', () => {
  expect(add(2, 3)).toBe(5);
  expect(add(10, 7)).toBe(17);
});

