$(document).ready(function() {
  // Handle form submission
  $('form').submit(function(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    
    // Get the product ID from the form
    var productID = $(this).find('input[name="product_id"]').val();
    
    // Send an AJAX request to add the product to the cart
    $.ajax({
      url: '/cart/add',
      method: 'POST',
      data: { product_id: productID },
      success: function(response) {
        // Update the cart count on the page
        $('#cart-count').text(response.cart_count);

        // Display a success message
        $('#message').text('Item added to cart');

        // Fetch and display the updated cart items
        fetchCartItems();
      },
      error: function(error) {
        // Handle error if the request fails
        console.log('Error occurred during adding item to cart.');
      }
    });
  });
});
