const IMG_FORMAT = "jpg";
const IMG_COUNT = 18;

const catLists = [];
for (let i = 0; i < IMG_COUNT; i++) {
  catLists.push(`${i}.${IMG_FORMAT}`);
}

const catNumber = Math.floor(Math.random() * IMG_COUNT);

const catImage = document.createElement("img");
catImage.src = `img/${catNumber}.${IMG_FORMAT}` 
catImage.classList.add("bg");

document.body.appendChild(catImage);