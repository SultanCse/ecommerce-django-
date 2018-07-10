from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart
from django.core.mail import send_mail
from django.db.models.signals import post_save
from cart.models import Cart, CartAmount
from products.models import ProductList
from order.utils import confirm_msg

# Create your models here.
class Order(models.Model):
    user     = models.ForeignKey(User)
    cart     = models.ForeignKey(Cart)
    transection = models.CharField(max_length=10)
    contact     = models.CharField(max_length=14)
    confirm     = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'order_number:' + str(self.id) +'    contact:' + self.contact + '    transection' + self.transection

def product_reduction_function(sender,instance, **kwargs):
    if instance.confirm ==  True:
        print(instance.cart)
        user = instance.user.first_name+" "+instance.user.last_name
        transection = instance.transection
        qs = CartAmount.objects.filter(cart=instance.cart)
        message = confirm_msg(user, transection)
        send_mail(
        'Order Confirmation',
        message,
        'microcir13@gmail.com',
        [instance.user.email],
        fail_silently=False,
            )
        print("sent success")
        print(instance.user.email)
        for product in qs:
            cart_amount = product.amount
            instance = ProductList.objects.get(id=product.products.id)
            in_stock =  instance.stock - cart_amount
            instance.stock = in_stock
            instance.save()


post_save.connect(product_reduction_function, Order)
