from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import NewFood, NewPizza, NewTopping, NewSalad, Item, NewPizzaNoTopping, NewPizza1Topping, NewPizza2Toppings, NewPizza3Toppings, NewPizzaSpecialInstructions
from .forms import ItemForm


def item(request, item_id):

    if not request.user.is_authenticated:
        form = AuthenticationForm()
        return render(request, "orders/login.html", {"message": "Welcome to Marko's Pizza & Subs! To see our item page, please login or register!", 'form':form})
    try:
        item = Item.objects.get(pk=item_id)
        print("item function item_id:", item_id)
        itemForm = ItemForm()
        itemForm.fields["_food"].queryset = NewFood.objects.filter(pk=item._food.id) # hide data
    except Item.DoesNotExist:
        raise Http404("Item does not exist")

    context = {
        "item": item,
        "itemForm": itemForm,
    }
    return render(request, "orders/item.html", context)


def v2menu(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        return render(request, "orders/login.html", {"message": "Welcome to Marko's Pizza & Subs! To see our menu page, please login or register!", 'form':form})

    context = {
        "user": request.user,
        # "items": Item.objects.all().order_by('_food___menuPosition'), # extra dunder between fields
        "items": Item.objects.all().order_by(Item.getFoodPosition()), # extra dunder between fiobject => data hiding
    }

    return render(request, "orders/itemMenu.html", context)
