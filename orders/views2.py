from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import NewFood, NewPizza, NewTopping, NewSalad, Item, NewPizzaNoTopping, NewPizza1Topping, NewPizza2Toppings, NewPizza3Toppings, NewPizzaSpecialInstructions, FoodPrice, Profile
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
        # itemForm.fields["_food"].queryset = NewFood.objects.filter(pk=20) # hide data
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


def itemsCard(request, user_id):
    user=request.user
    user_id=request.user.id
    context = {
        "items": Item.objects.filter(_user=user_id).all(),
        "user": user,
        "user_id": user_id
    }
    return render(request, "orders/itemsCard.html", context)


def addItem(request, item_id):
    user=request.user
    user_id=request.user.id
    # print("order function food_id:", food_id)
    item = Item.objects.get(pk=item_id)
    food = NewFood.objects.get(pk=item._food.id) # returns an object instance
    # food = NewFood.objects.filter(pk=item._food.id) # returns a list
    # price = FoodPrice.objects.get(pk=item._price.id)
    itemForm = ItemForm(request.POST)
    if itemForm.is_valid():
    # if food.model is NewFood:
    #     print("Heurekaaaaa!")
    # else:
    #     print("Noooo!")
        newItem = Item(
                        _food = itemForm.cleaned_data["_food"],
                        # _food = food,
                        _size = itemForm.cleaned_data["_size"],
                        _quantity = itemForm.cleaned_data["_quantity"],
                        # _price = price
                        )
        # print("newItem: ", newItem)
        newItem.save()
    context = {
        "items": Item.objects.filter(_user=user_id).all()
    }
    # return HttpResponseRedirect(reverse("orders"))# https://stackoverflow.com/questions/42466620/django-relationship-between-boundfield-and-form-field
    return render(request, "orders/itemsCard.html", context)
