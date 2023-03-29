const closeIcon = document.getElementById("close-icon");
const gallery = document.getElementById("gallery");
const gallery2 = document.getElementById("gallery2");
const images2 = gallery2.querySelectorAll(".image-cell");
const modal = document.getElementById("modal-container");
const images = gallery.querySelectorAll(".image-cell");
const videos = document.querySelectorAll(".video");
const videos2 = document.querySelectorAll(".video2");

const videosURL = ["xezer xeber.mp4"];
const videosURL2 = ["verlis1.m4v", "verlis2.m4v"];

const imagesURL = ["1.jpg", "2.jpeg", "3.jpeg", "4.jpeg", "5.jpeg", "6.jpeg"];
const images2URL = [
  "1.jpeg",
  "2.jpeg",
  "3.jpeg",
  "4.jpeg",
  "5.jpeg",
  "6.jpeg",
  "7.jpeg",
  "8.jpeg",
  "9.jpeg",
  "10.jpeg",
  "11.jpeg",
  "12.jpeg",
];
closeIcon.addEventListener("click", () => {
  console.log("HELLO");
  modal.style.display = "none";
  console.log(modal.children);
  if ("video-root" in modal.children) {
    modal.removeChild(modal.children["video-root"]);
  } else {
    modal.removeChild(modal.children["image-root"]);
  }
  modal.removeChild(modal.children["right-arrow"]);
  modal.removeChild(modal.children["left-arrow"]);
});
let index;

videos2.forEach(video => {
  video.addEventListener("click", () => {
    const rightArrow = document.createElement("img");
    rightArrow.classList.add("right-arrow");
    rightArrow.id = "right-arrow";
    rightArrow.src = "../static/images/index/right-arrow.png";

    const leftArrow = document.createElement("img");
    leftArrow.classList.add("left-arrow");
    leftArrow.id = "left-arrow";
    leftArrow.src = "../static/images/index/left-arrow.png";

    modal.style.display = "flex";
    let data = video.firstChild.nextSibling.src.split("/");
    console.log(data);
    let src =
      "../static/videos/" + data[data.length - 1].split(".")[0] + ".m4v";
    console.log(src);
    index = videosURL2.indexOf(data[data.length - 1].split(".")[0] + ".m4v");
    const node_video = document.createElement("video");
    node_video.id = "video-root";
    node_video.setAttribute("controls", "controls");
    node_video.setAttribute("autoplay", "autoplay");

    leftArrow.addEventListener("click", () => {
      index = index - 1 < 0 ? videosURL2.length - 1 : index - 1;
      let src = "../static/videos/" + videosURL2[index];
      const node_video = document.getElementById("video-root");
      node_video.src = src;
    });

    rightArrow.addEventListener("click", () => {
      index = index + 1 > videosURL2.length - 1 ? 0 : index + 1;
      let src = "../static/videos/" + videosURL2[index];
      console.log(index);
      const node_video = document.getElementById("video-root");
      node_video.src = src;
    });
    node_video.className = "modal-video";
    node_video.src = src;
    modal.append(rightArrow);
    modal.append(leftArrow);
    modal.append(node_video);
  });
});

videos.forEach(video => {
  video.addEventListener("click", () => {
    const rightArrow = document.createElement("img");
    rightArrow.classList.add("right-arrow");
    rightArrow.id = "right-arrow";
    rightArrow.src = "../static/images/index/right-arrow.png";

    const leftArrow = document.createElement("img");
    leftArrow.classList.add("left-arrow");
    leftArrow.id = "left-arrow";
    leftArrow.src = "../static/images/index/left-arrow.png";

    modal.style.display = "flex";
    let data = video.firstChild.nextSibling.src.split("/");
    let src =
      "../static/videos/" + data[data.length - 1].split(".")[0] + ".mp4";
    index = videosURL.indexOf(data[data.length - 1].split(".")[0] + ".mp4");
    const node_video = document.createElement("video");
    node_video.id = "video-root";
    node_video.setAttribute("controls", "controls");
    node_video.setAttribute("autoplay", "autoplay");

    leftArrow.addEventListener("click", () => {
      index = index - 1 < 0 ? videosURL.length - 1 : index - 1;
      let src = "../static/videos/" + videosURL[index];
      const node_video = document.getElementById("video-root");
      node_video.src = src;
    });

    rightArrow.addEventListener("click", () => {
      index = index + 1 > videosURL.length - 1 ? 0 : index + 1;
      let src = "../static/videos/" + videosURL[index];
      const node_video = document.getElementById("video-root");
      node_video.src = src;
    });
    node_video.className = "modal-video";
    node_video.src = src;
    modal.append(rightArrow);
    modal.append(leftArrow);
    modal.append(node_video);
  });
});

images.forEach(node => {
  node.addEventListener("click", () => {
    const rightArrow = document.createElement("img");
    rightArrow.classList.add("right-arrow");
    rightArrow.id = "right-arrow";
    rightArrow.src = "../static/images/index/right-arrow.png";

    const leftArrow = document.createElement("img");
    leftArrow.classList.add("left-arrow");
    leftArrow.id = "left-arrow";
    leftArrow.src = "../static/images/index/left-arrow.png";

    modal.style.display = "flex";
    let data = node.firstChild.nextSibling.src.split("/");
    let src = "../static/images/news/part 1/" + data[data.length - 1];
    index = imagesURL.indexOf(data[data.length - 1]);
    const node_image = document.createElement("img");
    node_image.id = "image-root";
    node_image.className = "modal-image";
    node_image.src = src;

    leftArrow.addEventListener("click", () => {
      index = index - 1 < 0 ? imagesURL.length - 1 : index - 1;
      console.log(index);
      let src = "../static/images/news/part 1/" + imagesURL[index];
      const node_image = document.getElementById("image-root");
      node_image.src = src;
    });

    rightArrow.addEventListener("click", () => {
      index = index + 1 > imagesURL.length - 1 ? 0 : index + 1;
      console.log(index);
      let src = "../static/images/news/part 1/" + imagesURL[index];
      const node_image = document.getElementById("image-root");
      node_image.src = src;
    });
    modal.append(node_image);
    modal.append(rightArrow);
    modal.append(leftArrow);
  });
});

images2.forEach(node => {
  node.addEventListener("click", () => {
    const rightArrow = document.createElement("img");
    rightArrow.classList.add("right-arrow");
    rightArrow.id = "right-arrow";
    rightArrow.src = "../static/images/index/right-arrow.png";

    const leftArrow = document.createElement("img");
    leftArrow.classList.add("left-arrow");
    leftArrow.id = "left-arrow";
    leftArrow.src = "../static/images/index/left-arrow.png";

    modal.style.display = "flex";
    let data = node.firstChild.nextSibling.src.split("/");
    let src = "../static/images/news/part 2/" + data[data.length - 1];
    index = images2URL.indexOf(data[data.length - 1]);
    const node_image = document.createElement("img");
    node_image.id = "image-root";
    node_image.className = "modal-image";
    node_image.src = src;

    leftArrow.addEventListener("click", () => {
      index = index - 1 < 0 ? images2URL.length - 1 : index - 1;
      let src = "../static/images/news/part 2/" + images2URL[index];
      const node_image = document.getElementById("image-root");
      node_image.src = src;
    });

    rightArrow.addEventListener("click", () => {
      index = index + 1 > images2URL.length - 1 ? 0 : index + 1;
      let src = "../static/images/news/part 2/" + images2URL[index];
      const node_image = document.getElementById("image-root");
      node_image.src = src;
    });
    modal.append(node_image);
    modal.append(rightArrow);
    modal.append(leftArrow);
  });
});