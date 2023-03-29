const imageContainer = document.getElementById("image-container");
const leftArrow = document.getElementById("left-arrow");
const rightArrow = document.getElementById("right-arrow");
const imageText = document.getElementById("image-header");
const content = document.getElementById("image-header-content");
const context = document.getElementById("context");
const interval = 10000;
const images = [
  "index/isfa main.jpg",
  "index/main-photo 2.jpg",
  "index/main-photo 3.jpeg",
  "index/main-photo 4.jpeg",
  "index/main-photo 5.jpeg",
  "index/main-photo 6.jpeg",
  "index/main-photo 7.jpeg",
  "index/main-photo 8.jpeg",
  "index/main-photo 9.jpeg",
];
var index = 0;

checkImageText = index => {
  if (index == 0) {
    imageText.style.opacity = 1;
    imageText.classList.remove("content");
    content.innerHTML = "ISFA";
    context.innerHTML = "GREEN LIFE";
  } else if (index == 1) {
    imageText.style.opacity = 1;
    imageText.classList.add("content");
    content.innerHTML = "Hər Növ Kənd Təsərrüfatları Xidməti";
    context.innerHTML = "Texnikalara 40% dövlət güzəşti";
  } else {
    imageText.classList.remove("content");
    imageText.style.opacity = 0;
  }
};

leftArrow.addEventListener("click", () => {
  index = index - 1 >= 0 ? index - 1 : images.length - 1;
  imageContainer.style.backgroundImage = `url('static/images/${images[index]}')`;
  imageContainer.classList.add("image-animation");
  leftArrow.disabled = true;
  clearInterval(myInterval);
  myInterval = setInterval(changeImage, interval);
  checkImageText(index);
  setTimeout(() => {
    imageContainer.classList.remove("image-animation");
    leftArrow.disabled = false;
  }, 700);
});

rightArrow.addEventListener("click", () => {
  index = index + 1 < images.length ? index + 1 : 0;
  imageContainer.style.backgroundImage = `url('static/images/${images[index]}')`;
  imageContainer.classList.add("image-animation");
  rightArrow.disabled = true;
  clearInterval(myInterval);
  myInterval = setInterval(changeImage, interval);
  checkImageText(index);
  setTimeout(() => {
    imageContainer.classList.remove("image-animation");
    rightArrow.disabled = false;
  }, 700);
});

imageContainer.style.backgroundImage = `url('static/images/${images[index]}')`;
let myInterval = setInterval(changeImage, interval);

function changeImage() {
  rightArrow.click();
}
