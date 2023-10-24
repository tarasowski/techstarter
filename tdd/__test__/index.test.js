// -> TDD aproach -> starts always with a test first and this test fails first
const { add, multiply, division } = require("../index")

test("an add function that sums up the numbers", () => {
    expect(add(1, 2)).toBe(3)
    // negate
    expect(add(1, 2)).not.toBe(4)
})

test("a multiply function that multiplies two numbers ", () => {
    expect(multiply(2,2)).toBe(4)
})

test("a division function that divides one number by the other one", () => {
    expect(division(4, 2)).toBe(2)
})

test('passes when value is NaN', () => {
    // innerhalb von einem Test können wir mehere expect haben
    expect(NaN).toBeNaN();
    expect(1).not.toBeNaN();
});

describe('arrayContaining', () => {
    const actual = ['Alice', 'Bob', 'Eve', 'Dimi']

    const expected = ['Alice', 'Bob'];

    it('matches even if received contains additional elements', () => {
      expect(actual).toEqual(expect.arrayContaining(expected));
    });

  });

test("test the length", () => {
    expect([1, 2, 3]).toHaveLength(3)
    expect([1, 2, 3, 4]).not.toHaveLength(3)
})