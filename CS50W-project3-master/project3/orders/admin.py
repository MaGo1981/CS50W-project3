from django.contrib import admin

from .models import Food, Pizza, Topping

admin.site.register(Food)
admin.site.register(Pizza)
admin.site.register(Topping)
