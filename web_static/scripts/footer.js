// Smooth scrolling for anchor links
$(document).on('click', 'a[href^="#"]', function(event) {
    event.preventDefault();
  
    $('html, body').animate({
      scrollTop: $($.attr(this, 'href')).offset().top
    }, 500);
  });
  
  // Show/hide mobile menu
  $('.mobile-menu-toggle').click(function() {
    $('.mobile-menu').slideToggle();
  });
  
  // Subscription form submission
  $('.subscription-form').submit(function(event) {
    event.preventDefault();
  
    var email = $('#email-input').val();
  
    // Validate email address
    if (email == '') {
      alert('Please enter your email address.');
      return;
    }
  
    if (!isValidEmail(email)) {
      alert('Please enter a valid email address.');
      return;
    }
  
    // Send form data to server
    $.ajax({
      type: 'POST',
      url: 'subscribe.php',
      data: { email: email },
      success: function(response) {
        alert(response);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        alert('An error occurred while subscribing. Please try again later.');
      }
    });
  });
  
  // Email address validation function
  function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
  