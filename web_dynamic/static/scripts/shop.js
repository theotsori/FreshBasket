document.addEventListener("DOMContentLoaded", function() {
    // Get category list and product list elements
    var categoryList = document.getElementById("category-list");
    var productList = document.getElementById("product-list");

    // Add click event listener to category list
    categoryList.addEventListener("click", function(event) {
        // Remove "active" class from all category items
        var categoryItems = categoryList.getElementsByTagName("li");
        for (var i = 0; i < categoryItems.length; i++) {
            categoryItems[i].classList.remove("active");
        }

        // Add "active" class to clicked category item
        var clickedItem = event.target;
        clickedItem.classList.add("active");

        // Get selected category
        var selectedCategory = clickedItem.dataset.category;

        // Show or hide products based on selected category
        var productItems = productList.getElementsByTagName("li");
        for (var j = 0; j < productItems.length; j++) {
            var productItem = productItems[j];

            if (selectedCategory === "all" || productItem.dataset.category === selectedCategory) {
                productItem.style.display = "block";
            } else {
                productItem.style.display = "none";
            }
        }
    });
});

// add to cart function
function addToCart(productId) {
    // Create an XMLHttpRequest object
    var xhr = new XMLHttpRequest();
  
    // Prepare the request URL
    var url = '/add_to_cart';
  
    // Prepare the request parameters
    var params = 'product_id=' + encodeURIComponent(productId);
  
    // Set up the request
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  
    // Define the callback function
    xhr.onload = function() {
      if (xhr.status === 200) {
        // Success: Update the cart dynamically
        var cartCount = document.getElementById('cart-count');
        var currentCount = parseInt(cartCount.innerText);
        cartCount.innerText = currentCount + 1;

        // Display success message

      } else {
        // Error: Display an error message
        alert('Error adding item to cart.');
      }
    };
  
    // Send the request
    xhr.send(params);
  }