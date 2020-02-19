from .import views
from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.urls import path,include


urlpatterns=[
    path('',views.home,name='home'), 
    path('home1/',views.home1,name='home1'),
    path('success/',views.success ,name='success'),
    path('cart/',views.cart ,name='cart'),
    path('removed/',views.removed,name='removed'),
    path('orders/',views.orders,name='orders'),
    path('place_orders/',views.place_orders,name='place_orders'),
    path('my_order/',views.my_order,name='my_order'),
    path('order_now/',views.order_now,name='order_now'),
    path('show/',views.show ,name='show'),
   #path('sign_up/',views.sign_up ,name='sign_up'),
 
 

    
]
