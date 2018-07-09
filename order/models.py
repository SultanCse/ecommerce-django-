from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart

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
        return str(self.id)
