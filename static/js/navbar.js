const navbar = document.getElementById("navbar");
const navbarLinks = document.getElementById("nav");
const toggleButton = document.querySelector(".toggle-button");
const navbarCloseIcon = document.querySelector(".navbar-close-icon");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky");
  } else {
    navbar.classList.remove("sticky");
  }
}

window.onscroll = function () {
  myFunction();
};

navbarCloseIcon.addEventListener("click", () => {
  navbarLinks.classList.remove("active");
});

toggleButton.addEventListener("click", () => {
  navbarLinks.classList.toggle("active");
});
