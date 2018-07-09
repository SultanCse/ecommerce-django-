from django.shortcuts import render, redirect
from cart.models import Cart, CartAmount
from django.http import JsonResponse
from cart.signals import calculate_cart_total
from django.http import HttpResponse, JsonResponse
from cart.models import CartAmount, Cart
from products.models import ProductCategory, ProductList

def cart_amount_to_total(request):
    if request.is_ajax():
        Cart.objects.cart_total(request)
        return JsonResponse({'ok':'ok'})

def amount_signal_in_cart_home(request):
    cart_id = request.session['cart_id']
    cart_obj = Cart.objects.get(id=cart_id)
    qs = CartAmount.objects.filter(cart=cart_obj)
    product_total = [{'id'      : product.id,
                  'title'       : product.title,
                  'img'         : product.image.url,
                  'price'       : product.price,
                  'amount'      : CartAmount.objects.get(products=product, cart=cart_obj).amount,
                  'total'       : CartAmount.objects.get(products=product, cart=cart_obj).total
                  } for product in cart_obj.products.all()]
    json_data = {
       'product_total': product_total,
       'shipping': cart_obj.shipping,
       'subtotal': cart_obj.subtotal,
       'total': cart_obj.total
    }
    return JsonResponse(json_data)


def cart_detail_api_view(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = [{
            "id": x.id,
            "title": x.title, 
            "price": x.price
            } 
            for x in cart_obj.products.all()]
    cart_data  = {"products": products, "subtotal": cart_obj.subtotal, "total": cart_obj.total}
    return JsonResponse(cart_data)

def cart_home(request):
    cat = ProductCategory.objects.all()
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_info = [{'id'          : product.id,
                  'title'       : product.title,
                  'img'         : product.image.url,
                  'price'       : product.price,
                  'in_stock'    : product.stock,
                  'amount'      : CartAmount.objects.get(products=product, cart=cart_obj).amount,
                  'total'       : CartAmount.objects.get(products=product, cart=cart_obj).total
                  } for product in cart_obj.products.all()]

    print(cart_info)
    print(cart_obj.total, cart_obj.subtotal, cart_obj.shipping)

    context ={
        'cart_info'     : cart_info,
        'total'         : cart_obj.total,
        'cart_subtotal' : cart_obj.subtotal,
        'shipping'      : cart_obj.shipping,
        'cat': cat
    }
    return render(request, "cart/home.html",context)


def cart_update(request):
    cat = ProductCategory.objects.all()
    product_id = request.POST.get('product_id')
    
    if product_id is not None:
        try:
            product_obj = ProductList.objects.get(id=product_id)
        except ProductList.DoesNotExist:
            # print("Show message to user, product is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            # cart_obj.products.remove(product_obj)
            CartAmount.objects.filter(products=product_id).delete()
            added = False
            calculate_cart_total.send(sender=cart_obj.__class__, instance=cart_obj)
        else:
            CartAmount.objects.create(
                                    products=product_obj,
                                    cart= cart_obj, 
                                    total = product_obj.price)
            added = True
            calculate_cart_total.send(sender=cart_obj.__class__, instance=cart_obj)
        request.session['in_cart'] = cart_obj.products.count()
        if request.is_ajax(): 
            json_data = {
                "added": added,
                "removed": not added,
                "items": cart_obj.products.count()
            }
            return JsonResponse(json_data)
    return redirect("cart:home")