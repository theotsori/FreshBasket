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


// Get the menu toggle button and menu
const menuToggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('.show-menu');

// Function to toggle the menu display
function toggleMenu() {
  menu.classList.toggle('show');
}

// Event listeners for logo and menu toggle button
document.querySelector('.logo a').addEventListener('click', toggleMenu);
menuToggle.addEventListener('click', toggleMenu);

// Call the function after the element is added to the DOM
window.addEventListener('DOMContentLoaded', initializeMenuToggle);