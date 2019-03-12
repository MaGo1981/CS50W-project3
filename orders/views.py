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
        "pizzas": Pizza.objects.all(),
        "toppings": Topping.objects.all(),
        "subs": Sub.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all(),
        "platters": Platter.objects.all()
    }

    return render(request, "orders/menu.html", context)

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
    print(food_id)
    try:
        # food_id = int(request.POST[food.name])
        # print("food_id:",food_id)
        # topping = Food.objects.get(pk=food_id)
        # print("topping:",topping)
        food = Food.objects.get(pk=food_id)
        allFood = Topping.objects.all()
    except Food.DoesNotExist:
        raise Http404("Food does not exist")
    context = {
        "food": food,
        "allFood": allFood
    }
    return render(request, "orders/food.html", context)

def order(request, food_id):
    try:
        user_id = int(request.POST["listedFood"])
        food = Food.objects.get(pk=food_id)
        user = User.objects.get(pk=user_id)
    except KeyError:
        return render(request, "orders/error.html", {"message": "No selection."})
    except Food.DoesNotExist:
        return render(request, "orders/error.html", {"message": "No food."})
    except User.DoesNotExist:
        return render(request, "orders/error.html", {"message": "No user."})
    user.foods.add(food)
    return HttpResponseRedirect(reverse("food", args=(food_id,)))
