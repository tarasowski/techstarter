console.log("start fetch")
let url = "https://jsonplaceholder.typicode.com/posts/1"


fetch(url, {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
}).then(response => response.json()) // -> this is an promsie)
  .then(response => console.log(response))


console.log("end fetch")