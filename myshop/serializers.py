from rest_framework import serializers
from myshop.models import Product,Addcart,Order_without_cart,Order


class Productform(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class Addcartform(serializers.ModelSerializer):
    class Meta:
        model=Addcart
        fields='__all__'


class Orderform(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

        
class Order_without_cartform(serializers.ModelSerializer):
    class Meta:
        model=Order_without_cart
        fields='__all__'
