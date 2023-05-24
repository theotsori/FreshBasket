// Function to handle adding a product to the cart
function addToCart(productId) {
    $.ajax({
      url: '/cart/add',
      method: 'POST',
      data: { product_id: productId },
      success: function(response) {
        // Update the cart count in the UI
        updateCartCount(response.cart_count);
      },
      error: function(error) {
        console.log('Error:', error);
      }
    });
  }

  // Function to update the cart count in the UI
  function updateCartCount(count) {
    $('#cart-count').text(count);
  }

  // Event delegation to handle the "Add to Cart" button click
  $('#product-list').on('click', '.add-to-cart-button', function(event) {
    event.preventDefault();
    var productId = $(this).siblings('[name="product_id"]').val();
    addToCart(productId);
  });