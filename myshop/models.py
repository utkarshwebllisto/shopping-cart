from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    pname = models.CharField(max_length = 100)
    image = models.ImageField()
    price = models.IntegerField()

    def __str__(self):
        return self.pname


class Addcart(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    pid = models.ForeignKey(Product, on_delete = models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.pid.pname


class Order(models.Model):
    quantity = models.IntegerField(default = 1)  
    owner = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    grand_total = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    user_phone = models.CharField(max_length=20, blank=True, null=True)
    user_address = models.CharField(max_length=20, blank=True, null=True)
    cart = models.ForeignKey(Product, on_delete = models.CASCADE, blank=True, null=True) 
    #cart = models.OneToOneField(Product, on_delete = models.CASCADE, blank=True, null=True) 


class Order_without_cart(models.Model):
  #  pid = models.ManyToManyField(Product, blank=True, null=True)
    costumer_name = models.CharField(max_length = 20,unique = True, blank=True, null=True)
    costumer_email = models.EmailField(max_length = 20, blank=True, null=True)
    costumer_phone = models.CharField(max_length = 20, blank=True, null=True)
    costumer_address = models.CharField(max_length = 20, blank=True, null=True)
    quantity = models.IntegerField()
    total_product = models.IntegerField()
    total_price = models.IntegerField()
