from django.urls import include, path
from django.contrib import admin
from shop.api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
 ]