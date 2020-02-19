from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import (render,
    redirect,
    HttpResponseRedirect,
    HttpResponse
)
# from shop.celery import debug_task,app
# from myshop.serializers import (ProductSerializer,
#     AddcartSerializer,
#     OrderSerializer,
#     Order_without_cartSerializer,
#     UserSerializer
# )
from myshop.models import (Product,
    Addcart,
    Order,
    Order_without_cart
)

from django.db import transaction
from .models import Profile
from .forms import UserForm,ProfileForm




def home(request):
    product_obj = Product.objects.all()
    return render(request,'account/mysite.html',{"product_obj": product_obj})


def home1(request):
    product_obj = Product.objects.all()
    return render(request,'account/mysite.html',{"product_obj": product_obj})



def success(request):
    context = {}
    context['user'] = request.user
    user = request.user.username
    product_obj = Product.objects.all()
    return render(request, "account/mysite.html", 
                  {"product_obj": product_obj})


# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('home1'))  



@login_required
def cart(request):
     if request.method == 'POST':
         quantity = request.POST["quantity"]
         obj_id = request.GET["id"]
         cart = Addcart.objects.filter(owner=request.user)
         if cart:
            cart.delete()
         username =request.user.username
         user_obj =User.objects.all()
         user_obj =  User.objects.get(username=username)
         product_obj = Product.objects.get(id=obj_id)
         cart = Addcart.objects.create(pid=product_obj,
                                       quantity=quantity,
                                       owner=user_obj)
     
     return HttpResponseRedirect(reverse('show'))


# @login_required
# def cart(request):
#      if request.method == 'POST':
#         quantity = request.POST["quantity"]
#         id = request.GET["id"]
#         product_obj = Product.objects.get(id = id)
#         try:
#             cart_obj_id = Addcart.objects.get(pid=id)
#             past_quantity=cart_obj_id.quantity
#         except:
#             pass
        
#         finally:
#             cart_obj = Addcart.objects.filter(owner=request.user)
#             cart_list=[]
#             price = product_obj.price   
#             product_list = []
#             for items in cart_obj: 
#                  product_list.append(items.pid.id)
#             if product_obj.id in product_list:
#                   return HttpResponse("this item is already in cart")
#             else:
#                   username = request.user.username
#                   user_obj =  User.objects.get(username=username)
#                   cart_obj = Addcart.objects.create(
#                                               pid=product_obj,
#                                               quantity=quantity,
#                                               owner=user_obj)
#      return redirect("/show")


@csrf_exempt
@login_required
def show(request):
    cart_obj = Addcart.objects.filter(owner=request.user)
    try:
        for items in cart_obj:
            obj_id = items.pid.id
            price = items.pid.price
            quantity = items.quantity
            total_price = price * quantity
        return render(
                    request, "mycart.html", {"cart_obj" : cart_obj, 'obj_id' : obj_id, 'total_price' : total_price })
    except:
        return render(
        request, "mycart.html", {"cart_obj": cart_obj})


#@login_required
#def show(request):
    # 
    # cart_obj = Addcart.objects.all()
    # cart_list = []
    # for items in cart_obj:
    #     cart_list.append(items.id)
    # #print(cart_list)
    # total_price = 0
    # for items in cart_obj:
    #     total_price = (total_price 
    #                    + items.total_price)
    # return render(
    #     request, "mycart.html", {"cart_obj": cart_obj, "total_price": total_price, 'cart_list': cart_list}
    # )


@login_required
@csrf_exempt
def orders(request):
    if (request.method) == 'POST':
        obj_id = request.POST['id']
        phone = request.POST['phone']
        Address = request.POST['Address']
        cart_obj = Addcart.objects.filter(owner=request.user)
        for items in cart_obj:
            quantity = items.quantity
            total_price = items.pid.price
        grand_total = int(quantity) * int(total_price)
        product_obj = Product.objects.get(id=obj_id)
        order = Order.objects.create(cart=product_obj,
                                     owner=request.user,
                                     quantity=quantity,
                                     grand_total=grand_total,
                                     username=request.user.username,
                                     user_phone=phone,
                                     user_address=Address)
        cart = Addcart.objects.filter(owner=request.user)
        cart.delete()
    return HttpResponseRedirect(reverse('my_order'))

      

@login_required
@csrf_exempt
def order_now(request):
    cart_items = Addcart.objects.filter(owner=request.user)
    for items in cart_items:
        obj_id = items.pid.id
        price = items.pid.price
        quantity = items.quantity
        total_price = price * quantity
    return render(
                  request, "order.html", {"cart_obj" : cart_items,
                                         "obj_id" : obj_id,
                                         "total_price" : total_price 
                                         })
  

# @login_required
# @csrf_exempt
# def orders(request):
#     if (request.method) == 'POST':
#         id = request.GET['id']
#         phone = request.POST['phone']
#         Address = request.POST['Address']
#         cart_obj = Addcart.objects.get(id=id)
#         cart_obj = cart_obj.id
#     cart = Addcart.objects.all()
#     total_product=0
#     for items in cart:
#         total_product+=items.quantity
#     username =request.user.username
#     return render(request,"order.html",{'cart': cart,
#                                         'total_price':total_price,
#                                         'total_product':total_product,
#                                         'username':username})
#      return redirect("/my_order")


@login_required
def place_orders(request):
    if request.method == "POST":
        total_product=request.POST['total_product']
        grand_total = request.POST['grand_total']
        user_name = request.user.username
        phone = request.POST['phone']
        Address = request.POST['Address']
        order_item = Order.objects.create(total_product=total_product,
                                            grand_total=grand_total,
                                            username=user_name,
                                            user_phone=phone,
                                            user_address=Address
                                            )
        order_item.save()
    return render(request, 'placed.html', {'username':user_name})


@login_required
def my_order(request):
    myorder= Order.objects.filter(owner=request.user)
    return render(request, 'myorder.html', {'myorder' : myorder})


@login_required
def removed(request):
    id = request.GET["id"]
    cart_obj = Addcart.objects.get(id = id)
    cart_obj.delete()
    return HttpResponseRedirect(reverse('success'))

