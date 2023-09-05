const customerInfo = {
    name: "Dimi",
    id: 1,
    address: "Berlinerweg",
    changeAddress: function() {
        this.address = "New Address"
        return this.address
    } 
}

// delete a property from an object

//delete customerInfo.id

// destructuring
const { id, name, ...customerInfoNew } = customerInfo // customerInfo stays the same, will not be modified (mutated)
const [head, secondElement, ...rest] = [1,2,3,4,5,6]
const [firstChar, ...allChars] = "Hello"

console.log(
    //customerInfo.changeAddress()
    //id,
    //customerInfoNew,
    //customerInfo
    //head,
    //rest,
    //firstChar,
    //allChars

)


/*
const Car = function() {
    this.color = "black"
}

[1,2,3,4,5].filter()
Array.prototype.filter = function() {
    // for loop
}

[1,2,3,5].map()
Array.prototype.map = function() {
    // for loop
}

Car.prototype.drive = function() {
    //...Car.
}
*/

// destructuring


function customerOrder({name, adddress, id}) {
    // code comes here
    console.log("name", name)
    console.log("adddress", address)
    console.log("id", id)
}

customerOrder({name: "Dimi", address: "Berlinerweg", id: 1})