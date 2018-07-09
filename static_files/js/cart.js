$(document).ready(function(){
    var productForm = $(".form-product-ajax") // #form-product-ajax
    productForm.submit(function(event){
        event.preventDefault();
        // console.log("Form is not sending")
        var thisForm = $(this)
        // var actionEndpoint = thisForm.attr("action"); // API Endpoint
        var actionEndpoint = thisForm.attr("data-endpoint")
        var httpMethod = thisForm.attr("method");
        var formData = thisForm.serialize();
        var currentPath = window.location.href
        $.ajax({
          url: actionEndpoint,
          method: httpMethod,
          data: formData,
          success: function(data){
            var submitSpan = thisForm.find(".submit-span");
            if (currentPath.indexOf("details") == -1) {
              if (data.added){
                submitSpan.html("<button type='submit' class='btn btn-danger btn-block'>Remove</button>")
              } else {
                    submitSpan.html('<button type="submit" class="btn btn-primary btn-block">Cart</button>')
               }
            }
            else{
              if (data.added){
                submitSpan.html("<button type='submit' class='btn btn-danger btn-block'>Remove</button>")
              } else {
                submitSpan.html('<button type="submit" class="btn btn-primary btn-block">Cart</button>')
               }
            }
            var navbarCount = $(".navbar-cart-count")
            navbarCount.text(data.items)
            if (currentPath.indexOf("cart") != -1) {
              // refreshCart()
              window.location.href = currentPath
            }
          },
          error: function(errorData){
            console.log("error")
            console.log(errorData)
          }
        })
    })
    function refreshCart(){
      console.log("in current cart")
      var cartTable = $(".cart-table")
      var cartBody = cartTable.find(".cart-body")
      var productRows = cartBody.find(".cart-product")
      var currentUrl = window.location.href
      var refreshCartUrl = '/carts/api/cart/'
      var refreshCartMethod = "GET";
      var data = {};
      $.ajax({
        url: refreshCartUrl,
        method: refreshCartMethod,
        data: data,
        success: function(data){
          
          var hiddenCartItemRemoveForm = $(".cart-item-remove-form")
          if (data.products.length > 0){
              productRows.html(" ")
              i = data.products.length
              $.each(data.products, function(index, value){
                // console.log(value)
                var newCartItemRemove = hiddenCartItemRemoveForm.clone()
                newCartItemRemove.css("display", "block")
                newCartItemRemove.find(".cart-item-product-id").val(value.id)
                  cartBody.prepend("<tr><th scope=\"row\">" + i + "</th><td><a href='" + value.url + "'>" + value.title + "</a>" + newCartItemRemove.html() + "</td><td>" + value.price + "</td></tr>")
                  i --
              })
              
              cartBody.find(".cart-subtotal").text(data.subtotal)
              cartBody.find(".cart-total").text(data.total)
          } else {
            window.location.href = currentUrl
          }
          
        },
        error: function(errorData){
          console.log("error")
          console.log(errorData)
        }
      })
    }
  })