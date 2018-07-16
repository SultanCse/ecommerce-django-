from order.models import Order
from django import forms

class OrderForm(forms.Form):
    contact = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 
                "id": "form_full_name", 
                "placeholder": "your contact number"}))
    transection = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 
                "id": "form_full_name", 
                "placeholder": "your bkash transection number"}))

class OrderConfrimForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['confirm']
     