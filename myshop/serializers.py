from rest_framework import serializers
from django.contrib.auth.models import User
from myshop.models import Product,Addcart,Order_without_cart,Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class AddcartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Addcart
        fields='__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

        
class Order_without_cartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order_without_cart
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
