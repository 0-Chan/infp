const todoWrap = document.querySelector("#todo-wrap");
const todoForm = document.querySelector("#todo-form");
const todoInput = document.querySelector("#todo-form input");
const todoList = document.querySelector("#todo-list")

const TODOS_KEY = "todos";
let todos = [];

function paintTodo(newTodo) {
  const todoItems = document.createElement("li");
  const todoContent = document.createElement("span");
  const todoDelete = document.createElement("button");

  todoItems.appendChild(todoContent);
  todoItems.appendChild(todoDelete);
  
  todoItems.id = newTodo.id;
  todoContent.innerText = newTodo.text;
  todoDelete.innerText = "⛔";
  
  todoDelete.addEventListener("click", handelDeleteClick);

  todoList.appendChild(todoItems);
}

function handleTodoSubmit(event) {
  event.preventDefault();
  const newTodo = todoInput.value;
  todoInput.value = "";

  const newTodoObj = {
    text: newTodo,
    id: Date.now(),
  };

  todos.push(newTodoObj);
  paintTodo(newTodoObj);
  saveTodo();
}

function handelDeleteClick(event) {
  event.preventDefault();
  const combinedItem = event.target.parentElement;

  todos = todos.filter(todo => todo.id !== parseInt(combinedItem.id));
  saveTodo();

  combinedItem.remove();
}

function saveTodo() {
  localStorage.setItem(TODOS_KEY, JSON.stringify(todos));
}

todoForm.addEventListener("submit", handleTodoSubmit);

const savedTodos = localStorage.getItem(TODOS_KEY);
if (savedTodos !== null) {
  const parsedTodos = JSON.parse(savedTodos);
  todos = parsedTodos;
  parsedTodos.forEach(paintTodo);    
} else if (savedTodos === null) {
  console.log("emptyyyy null!!!")
}