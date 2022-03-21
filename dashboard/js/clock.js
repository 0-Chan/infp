const mainClock = document.querySelector(".js-clock");
const ddayClock = document.querySelector(".dday-clock");
const d_day = new Date('2022-05-05T00:00:00');

function getClock() {
  let current_day = new Date();
  let subtract_sec = (d_day.getTime() - current_day.getTime())/1000;

  let year_now = current_day.getFullYear();
  let month_now = current_day.getMonth() + 1;
  let date_now = current_day.getDate();
  let hours_now = String(current_day.getHours()).padStart(2, "0");;
  let minutes_now = String(current_day.getMinutes()).padStart(2, "0");;
  let seconds_now  = String(current_day.getSeconds()).padStart(2, "0");;

  let days_left = Math.floor(subtract_sec / 60 / 60 / 24);
  let hours_left = Math.floor(subtract_sec / 60 / 60 % 24);
  let minutes_left = Math.floor(subtract_sec / 60 % 60);
  let seconds_left = Math.floor(subtract_sec % 60 % 60 % 60);
  
  mainClock.innerHTML = `${year_now}. ${month_now}. ${date_now} ${hours_now}:${minutes_now}:${seconds_now}`;
  ddayClock.innerHTML = `${days_left}d ${hours_left}h ${minutes_left}m ${seconds_left}s until next 빨간날… (어린이날!)`;
}

setInterval(getClock, 1000);