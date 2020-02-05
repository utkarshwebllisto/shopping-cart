from django.contrib import admin
from django.contrib import admin
from myshop.models import (Product,
	                        Addcart,
	                        Order,
	                        Order_without_cart)

admin.site.register(Product)

admin.site.register(Addcart)

admin.site.register(Order)

admin.site.register(Order_without_cart)

