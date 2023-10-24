const { main } = require("../main")

test("test the main function", () => {
    expect(main({name: "Pablo", age: 30})).toBe("Hallo Pablo!")
})