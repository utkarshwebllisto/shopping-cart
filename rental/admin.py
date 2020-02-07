from django.contrib import admin

# Register your models here.

from rental.models import (Friend,
	                        Belonging,
	                        Borrowed,
	                        )

admin.site.register(Friend)
admin.site.register(Belonging)
admin.site.register(Borrowed)