document.getElementById('signin-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
  
    // Send the data to the server for validation
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'signin.php', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        if (response.success) {
          // User successfully authenticated, redirect to another page or perform other actions
          console.log('User authenticated!');
        } else {
          // Authentication failed, display an error message
          console.log('Authentication failed:', response.message);
        }
      }
    };
    xhr.send('email=' + encodeURIComponent(email) + '&password=' + encodeURIComponent(password));
  });
  