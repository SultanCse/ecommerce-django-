from order.models import Order
from django import forms

class OrderForm(forms.Form):
    contact = forms.CharField()
    transection = forms.CharField()
     