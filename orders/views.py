from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User


from .models import Food, Pizza, Topping, Sub, Pasta, Salad, Platter

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/register.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "orders/index.html", context)

def menu(request):
    context = {
        "pizzas": Pizza.objects.exclude(menu=False).all(),
        "toppings": Topping.objects.exclude(menu=False).all(),
        "subs": Sub.objects.exclude(menu=False).all(),
        "pastas": Pasta.objects.exclude(menu=False).all(),
        "salads": Salad.objects.exclude(menu=False).all(),
        "platters": Platter.objects.exclude(menu=False).all()
    }

    return render(request, "orders/menu.html", context)

def orders(request):
    context = {
        "pizzas": Pizza.objects.exclude(menu=True).all(),
        "toppings": Topping.objects.exclude(menu=True).all(),
        "subs": Sub.objects.exclude(menu=True).all(),
        "pastas": Pasta.objects.exclude(menu=True).all(),
        "salads": Salad.objects.exclude(menu=True).all(),
        "platters": Platter.objects.exclude(menu=True).all()
    }

    return render(request, "orders/orders.html", context)

def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def register_view(request):
    username1 = request.POST.get("username1")
    email1 = request.POST.get("email1")
    password1 = request.POST.get("password1")
    repeatPassword1 = request.POST.get("repeat-password1")
    # user1 = User.objects.create_user("alice", "alice@something.com", "alice12345")
    user1 = User.objects.create_user(username=username1, email=email1, password=password1)
    if user1 is not None:
        user1.save()
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "orders/register.html", {"message": "Invalid credentials."})

def food(request, food_id):
    print("food function food_id:", food_id)

    try:
        food = Food.objects.get(pk=food_id)
        allToppings = Topping.objects.exclude(menu=False).all()
        print("food function allToppings:", allToppings)
        pizzas = Pizza.objects.exclude(menu=False).all()
        print("food function pizzas:", pizzas)
        quantity = food.quantity
        print("food.quantity:", quantity)
    except Food.DoesNotExist:
        raise Http404("Food does not exist")
    context = {
        "food": food,
        "allToppings": allToppings,
        "pizzas": pizzas
    }
    return render(request, "orders/food.html", context)


def order(request, food_id):
    print("order function food_id:", food_id)
    food = Food.objects.get(pk=food_id)
    print("order function food:", food)

    try:
        topping_id = int(request.POST["topping"])
        quantity = int(request.POST["quantity"])
        size = request.POST["size"]
        print("order function topping_id:",topping_id)
        topping = Topping.objects.get(pk=topping_id)
        print("order function topping:",topping)
        order = Pizza(name=food, topping1=topping, topping2=topping, topping3=topping, quantity=quantity, size=size)
        order.save()

    except KeyError:
        return render(request, "orders/error.html", {"message": "No selection."})
    except Food.DoesNotExist:
        return render(request, "orders/error.html", {"message": "No food."})
    except Topping.DoesNotExist:
        return render(request, "orders/error.html", {"message": "No topping."})
    # user.foods.add(food)
    return HttpResponseRedirect(reverse("orders"))
