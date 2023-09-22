const url = "https://jsonplaceholder.typicode.com/posts/1"


async function callApi() {
    const response = await fetch(url, {method: "GET", headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }});
    const data = await response.json();
    console.log(data)
    return data;
}

callApi()

