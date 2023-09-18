const url = "https://api.brightsky.dev/weather?lat=52.52&lon=13.404954&date=2023-09-13"

const getWeather = () => {
   return fetch(url).then(response => response.json())
             .then(console.log)
             .catch(console.error)
}

const getWeather2 = async () => {
    const response = await fetch(url) 
    const body = await response.json()
    return body
}

getWeather()