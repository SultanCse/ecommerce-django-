from django.shortcuts import render, get_object_or_404
from products.models import ProductList
from cart.models import Cart, CartAmount

# Create your views here.

def show_products_list(request):
    products_list = ProductList.objects.all()
    context = {
        'products_list_all': products_list
    }
    return render(request, 'products/home.html', context)


def product_detail(request, pk):
    product_detail = get_object_or_404(ProductList, id=pk)
    cart_obj, new_cart = Cart.objects.new_or_get(request)
    cart_amount_instance = CartAmount.objects.filter(products=product_detail, cart=cart_obj)
    cart_amount_count = 1
    if cart_amount_instance.count() > 0:
        for x in cart_amount_instance:
            cart_amount_count = x.amount 
    context={
        'product_item_detail': product_detail, 
        'cart': cart_obj,
        'cart_amount_count': cart_amount_count
    }
    return render(request, 'products/product-detail.html', context)

def featured_list(request):
    products_list = ProductList.objects.filter(featured=True)
    context = {
        'products_list_all': products_list
    }
    return render(request, 'products/home.html', context)
