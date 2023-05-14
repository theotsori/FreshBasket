// select the menu toggle button
const menuToggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('nav.show-menu');

  menuToggle.addEventListener('click', () => {
    nav.classList.toggle('active');
  });