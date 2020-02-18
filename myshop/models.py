from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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
