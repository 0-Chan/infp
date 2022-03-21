const weatherDiv = document.querySelector("#weather");

const API_KEY = "5725c80a489268cab6b09cc66a2f5111";
const lang = "kr";

function onGeoOk(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;

  // const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}`;
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&lang=${lang}&units=metric`
  fetch(url).then(response => response.json().then(data => {
    const city = document.querySelector("#weather span:first-child")
    const weather = document.querySelector("#weather span:last-child")

    console.dir(city);
    console.dir(weather);

    city.innerHTML = data.name;
    weather.innerHTML = `${data.weather[0].main} / ${data.main.temp}℃`;

    console.log(city.innetHTML, weather.innetHTML);
  }));
}
function onGeoError() {
  alert("Cannot get geo");
}

navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);