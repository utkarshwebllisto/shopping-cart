from django import forms
from .models import Product,Addcart,Order_without_cart,Order


class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'


class Addcartform(forms.ModelForm):
    class Meta:
        model=Addcart
        fields='__all__'


class Orderform(forms.ModelForm):
    class Meta:
        model=Order
        fields='__all__'

        
class Order_without_cartform(forms.ModelForm):
    class Meta:
        model=Order_without_cart
        fields='__all__'
