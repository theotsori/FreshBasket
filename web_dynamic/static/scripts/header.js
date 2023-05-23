// select the menu toggle button
function initializeMenuToggle() {
  var menuToggle = document.querySelector('.menu-toggle');
  if (menuToggle) {
    menuToggle.addEventListener('click', function() {
      var nav = document.querySelector('nav');
      if (nav) {
        nav.classList.toggle('show-menu');
      }
    });
  }
}

// Call the function after the element is added to the DOM
window.addEventListener('DOMContentLoaded', initializeMenuToggle);