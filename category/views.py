from django.shortcuts import render, get_object_or_404
from products.models import ProductList, ProductCategory
from cart.models import Cart

def show_category_products_list(request, categoryy):
    cart_obj, new_cart = Cart.objects.new_or_get(request)
    # pro_category = ProductCategory.objects.get(title=category)
    pro_category = get_object_or_404(ProductCategory,title=categoryy)
    query = ProductList.objects.filter(category=pro_category)
    context = {
        'products_list_all' : query,
        'cart': cart_obj,
    }
    return render(request, 'category_view/category_view.html', context)