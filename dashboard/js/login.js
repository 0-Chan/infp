const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greetingMessage = document.querySelector("#greeting-msg");

const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "userName";

const nameOfUser = localStorage.getItem(USERNAME_KEY);

function handleLoginSubmit(event) {
  event.preventDefault();
  const userName = loginInput.value;

  localStorage.setItem(USERNAME_KEY, userName)
  paintGreetings();
}

function greetingCount() {
  greetingMessage.insertAdjacentHTML("beforeend", ".");
}


function greetingOver() {
  greetingMessage.classList.add(HIDDEN_CLASSNAME);
  todoWrap.classList.remove(HIDDEN_CLASSNAME);
}

function paintGreetings() {
  const userName = localStorage.getItem(USERNAME_KEY);
  
  loginForm.classList.add(HIDDEN_CLASSNAME);
  greetingMessage.classList.remove(HIDDEN_CLASSNAME);

  mainClock.classList.remove(HIDDEN_CLASSNAME);
  ddayClock.classList.remove(HIDDEN_CLASSNAME);
  weatherDiv.classList.remove(HIDDEN_CLASSNAME);

  greetingMessage.innerText = `Hello, ${userName}`;
  setInterval(greetingCount, 1000);
  setTimeout(greetingOver, 3500);
}

if (nameOfUser === null) {
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", handleLoginSubmit);
} else {
  paintGreetings();
}