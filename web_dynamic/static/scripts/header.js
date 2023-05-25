// Get references to the form and input element
const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');

// Add an event listener to the form submission
searchForm.addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent the form from submitting normally

  const query = searchInput.value; // Get the entered query
  const url = `/search?query=${encodeURIComponent(query)}`; // Create the URL with the query parameter

  window.location.href = url; // Redirect to the search URL
});


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