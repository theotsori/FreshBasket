document.getElementById('shipping-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    var form = this;
    
    // Submit the form asynchronously
    var xhr = new XMLHttpRequest();
    xhr.open(form.method, form.action, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        // Form submission successful, redirect to checkout page
        window.location.href = "{{ url_for('checkout') }}";
      }
    };
    xhr.send(new FormData(form));
  });