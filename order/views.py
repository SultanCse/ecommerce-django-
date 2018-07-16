from django.shortcuts import render, redirect
from order.forms import OrderForm, OrderConfrimForm
from order.models import Order
from cart.models import Cart, CartAmount
from products.models import ProductList

def order(request):
    form = OrderForm(request.POST or None)
    context = {
        'form' : form
    }
    if form.is_valid():
        transection = form.cleaned_data.get('transection')
        contact = form.cleaned_data.get('contact')
        cart_id = request.session.get("cart_id")
        cart_instance = Cart.objects.get(id=cart_id)
        Order.objects.create(
            user=request.user,
            cart=cart_instance,
            transection=transection,
            contact=contact
        )
        return redirect('order:confirm')        
    return render(request, 'order/order.html', context)

def confirm(request):
    del request.session['in_cart']
    del request.session['cart_id']
    return render(request, 'order/notify.html')

def admin_order(request):#order list joma hobe
    orders = Order.objects.filter(confirm=False)
    context={
        'orders': orders
    }
    return render(request, 'order/admin_order.html', context)

def detail(request, pk): #order details
    order = Order.objects.get(id=pk)
    form = OrderConfrimForm(request.POST or None, instance=order)
    cart_amount = CartAmount.objects.filter(cart=order.cart)
    context={
        'order': order,
        'form': form,
        'cart_amount': cart_amount
    }
    print('Look here: ',order.user.username)
    if request.method == 'POST' and form.is_valid():
        form.save() 
        return redirect('order:order')
    return render(request, 'order/admin_detail.html',context)

