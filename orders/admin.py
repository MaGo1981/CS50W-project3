from django.contrib import admin

from .models import Food, Pizza, Topping, Sub, Pasta, Salad, Platter, NewFood, NewPizza, NewPizza1Topping, NewPizza2Toppings, NewPizza3Toppings, NewPizzaNoTopping, NewPizzaSpecialInstructions, NewTopping, NewSalad, FoodPrice, Item, Order


admin.site.register(Food)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Platter)
admin.site.register(NewFood)
# admin.site.register(NewPizza)
admin.site.register(NewTopping)
admin.site.register(NewSalad)
admin.site.register(FoodPrice)
# admin.site.register(PizzaPrice)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(NewPizza1Topping)
admin.site.register(NewPizza2Toppings)
admin.site.register(NewPizza3Toppings)
admin.site.register(NewPizzaNoTopping)
admin.site.register(NewPizzaSpecialInstructions)
