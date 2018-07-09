from django.db import models
from django.contrib.auth.models import User
from products.models import ProductCategory, ProductList
from cart.signals import calculate_cart_total

class CartManager(models.Manager):
    
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)

    def cart_total(self, request):
        cart_product_id = request.POST.get('produt-cart-name')
        cart_product_obj = ProductList.objects.get(id=cart_product_id)
        cart_id = request.session['cart_id']
        cart_obj = Cart.objects.get(id=cart_id)
        product_price = cart_product_obj.price
        cart_amount = request.POST.get('qty-name')
        total = float(product_price) * float(cart_amount)
        instance = CartAmount.objects.filter(products=cart_product_obj, cart=cart_obj)
        if instance.count() == 1:
            instance = instance.first()
            instance.total = total
            instance.amount = cart_amount
            instance.save()
            calculate_cart_total.send(sender=cart_obj.__class__, instance=cart_obj)
      


class Cart(models.Model):
    user        = models.ForeignKey(User, null=True)
    products    = models.ManyToManyField(ProductList, through='CartAmount',blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    shipping    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    objects     = CartManager()

    def __str__(self):
        return str(self.id)

class CartAmount(models.Model):
    cart    = models.ForeignKey(Cart)
    products  = models.ForeignKey(ProductList)
    amount  = models.IntegerField(default=1)
    total   = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
    


def m2m_changed_receiver(sender, instance, *args, **kwargs):
    cart_id  = instance.id
    products = CartAmount.objects.filter(cart=cart_id)
    total = 0
    for product in products:
        total += product.total
    instance.subtotal = total
    if total < 1000:
        instance.shipping = 100
    elif total < 2000:
        instance.shipping = 100
    else:
        instance.shipping = 0
    instance.total = instance.subtotal + instance.shipping
    instance.save()

calculate_cart_total.connect(m2m_changed_receiver)
