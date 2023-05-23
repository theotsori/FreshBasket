// Select the slideshow element
var slideIndex = 0;
var slides = document.getElementsByClassName("slides");

setInterval(function() {
  slideIndex++;
  if (slideIndex >= slides.length) {
    slideIndex = 0;
  }
  for (var i = 0; i < slides.length; i++) {
    slides[i].style.opacity = 0;
  }
  slides[slideIndex].style.opacity = 1;
}, 5000);
