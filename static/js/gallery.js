const modal = document.getElementById("modal-container");
const videos = document.querySelectorAll(".video");
const images = document.querySelectorAll(".image-cell");
const closeIcon = document.getElementById("close-icon");
const gallery = document.getElementById("gallery");

const videosURL = ["yevlax.mp4", "main.mp4", "qusar.mp4"];
const imagesURL = [
  "main-photo-1.jpeg",
  "main-photo-2.jpeg",
  "main-photo-3.jpeg",
  "main-photo-4.jpeg",
  "main-photo-5.jpeg",
  "main-photo-6.jpeg",
  "main-photo-7.jpg",
  "main-photo-8.jpg",
  "main-photo-9.jpg",
  "main-photo-10.jpg",
  "main-photo-11.jpg",
  "main-photo-12.jpg",
  "main-photo-13.jpg",
  "main-photo-14.jpg",
  "main-photo-15.jpeg",
  "main-photo-16.jpeg",
  "main-photo-17.jpeg",
  "main-photo-18.jpeg",
  "main-photo-19.jpeg",
  "main-photo-20.jpeg",
  "main-photo-21.jpeg",
  "main-photo-22.jpeg",
  "main-photo-23.jpeg",
  "main-photo-24.jpeg",
  "main-photo-25.jpeg",
];
let index;

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
    // node_video.setAttribute("autofocus", "autofocus");
    // node_video.setAttribute("autoplay", "autoplay");

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

closeIcon.addEventListener("click", () => {
  modal.style.display = "none";
  if ("video-root" in modal.children) {
    modal.removeChild(modal.children["video-root"]);
  } else {
    modal.removeChild(modal.children["image-root"]);
  }
  modal.removeChild(modal.children["right-arrow"]);
  modal.removeChild(modal.children["left-arrow"]);
  console.log(modal.children);
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
    let src = "../static/images/gallery/" + data[data.length - 1];
    index = imagesURL.indexOf(data[data.length - 1]);
    console.log(index);
    const node_image = document.createElement("img");
    node_image.id = "image-root";
    node_image.className = "modal-image";
    node_image.src = src;

    leftArrow.addEventListener("click", () => {
      index = index - 1 < 0 ? imagesURL.length - 1 : index - 1;
      console.log(index);
      let src = "../static/images/gallery/" + imagesURL[index];
      const node_image = document.getElementById("image-root");
      node_image.src = src;
    });

    rightArrow.addEventListener("click", () => {
      index = index + 1 > imagesURL.length - 1 ? 0 : index + 1;
      console.log(index);
      let src = "../static/images/gallery/" + imagesURL[index];
      const node_image = document.getElementById("image-root");
      node_image.src = src;
    });
    modal.append(node_image);
    modal.append(rightArrow);
    modal.append(leftArrow);
  });
});
