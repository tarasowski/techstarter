const url = "https://api.brightsky.dev/weather?lat=52.52&lon=13.404954&date=2023-09-13"


const getWeather = () => {
   fetch(url).then(async response => {
    if (response.status === 200) {
        const body = await response.json()
        return body
    } else {
        console.error("request has failed")
    }
   }).catch(error => console.log(error))
   return null
}

const getWeather2 = async () => {
    const response = await fetch(url) 
    const body = await response.json()
    console.log(body)
    return body
}

getWeather2()