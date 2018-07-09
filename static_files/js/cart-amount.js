$('document').ready(function(){
    var currentpath;
function refreshCartHome(){
    $.ajax({
        method: 'GET',
        url: '/carts/api/cart/siganl/',
        data:{},
        success: function(data){
            console.log('success yeah');
            window.location.href = currentpath
        },
        error: function(errorData){
            console.log('error');
            console.log(errorData)
        }
    })
}

$('.quantity-form').mouseleave(function(){;
    var parentClass = $(this).serializeArray();
    dataObj = {};
    $.each(parentClass, function(i, field){
        dataObj[field.name] = field.value;
    });
    console.log(dataObj['in-stock-amount'], dataObj['qty-name'])
    if (parseInt(dataObj['in-stock-amount']) < parseInt(dataObj['qty-name'])){
        $(this).find('p').text('Only '+ dataObj['in-stock-amount'] + ' in stock');
    }else{
    $(this).find('p').text('')
    $.ajax({
        url: '/carts/api/cart/total/',
        data: $(this).serialize(),
        method: 'POST',
        success:function(data){
            console.log('success');
            currentpath = window.location.href
            if (currentpath.indexOf('carts') != -1){
                refreshCartHome()
            }
        },
        error: function(errorData){
            console.log(errorData);
        }
    })
}
})


})
