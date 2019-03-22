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
    # print("food function food_id:", food_id)

    try:
        food = Food.objects.get(pk=food_id)
        allToppings = Topping.objects.exclude(menu=False).all()
        # print("food function allToppings:", allToppings)
        pizzas = Pizza.objects.exclude(menu=False).all()
        # print("food function pizzas:", pizzas)
        quantity = food.quantity
        # print("food.quantity:", quantity)
        subs = Sub.objects.exclude(menu=False).all()

    except Food.DoesNotExist:
        raise Http404("Food does not exist")
    context = {
        "food": food,
        "allToppings": allToppings,
        "pizzas": pizzas,
        "subs": subs
    }
    return render(request, "orders/food.html", context)


def order(request, food_id):
    # print("order function food_id:", food_id)
    food = Food.objects.get(pk=food_id)
    user=request.user
    # print("order function food:", food)
    # print(issubclass(Pizza, Food))
    # print(isinstance(food, Pizza)) # vraca False kad narucujem pizzu, a trebalo bi vracati True
    # print(isinstance(pizza, Pizza))
    # print("food.pizza:", food.pizza) #vraca pizzu s menu-a ili vraca gresku ako narucujes topping
    # print("food.topping:", food.topping ) # obrnuto od food.pizza

    try:
        pizza = Pizza.objects.get(pk=food_id)
        if isinstance(pizza, Pizza):
            topping1_id = int(request.POST["topping-whole"]) # kad se radi o ForeignKey property klase, mora ici po id jer ForeignKey je uvijek ID!!!
            topping2_id = int(request.POST["topping-left"]) # kad se radi o ForeignKey property klase, mora ici po id jer ForeignKey je uvijek ID!!!
            topping3_id = int(request.POST["topping-right"])# kad se radi o ForeignKey property klase, mora ici po id jer ForeignKey je uvijek ID!!!
            quantity = int(request.POST["quantity"])
            size = request.POST["size"]
            specialInstructions = request.POST["specialInstructions"]
            print("order function topping1_id:",topping1_id)
            print("order function specialInstructions:",specialInstructions)
            topping1 = Topping.objects.get(pk=topping1_id)
            topping2 = Topping.objects.get(pk=topping2_id)
            topping3 = Topping.objects.get(pk=topping3_id)
            print("order function topping1:",topping1)
            order = Pizza(name=food, topping1=topping1, topping2=topping2, topping3=topping3, quantity=quantity, size=size, specialInstructions=specialInstructions, user=user)
            order.save()


    except KeyError:
        return render(request, "orders/error.html", {"message": "No selection, no id."})
    except Pizza.DoesNotExist:
        try:
            topping = Topping.objects.get(pk=food_id)
            if isinstance(topping, Topping):
                quantity = int(request.POST["quantity"])
                specialInstructions = request.POST["specialInstructions"]
                side = request.POST["side"]
                order = Topping(name=food, quantity=quantity, specialInstructions=specialInstructions, side=side, user=user)
                order.save()
        except Topping.DoesNotExist:
            try:
                sub = Sub.objects.get(pk=food_id)
                if isinstance(sub, Sub):
                    quantity = int(request.POST["quantity"])
                    size = request.POST["size"]
                    specialInstructions = request.POST["specialInstructions"]
                    name=food.name
                    print('sub name', name)
                    if name=='Meatball':
                        if size == 'small':
                            order = Sub(name=food, quantity=quantity, size=size, specialInstructions=specialInstructions, user=user, price=6.50)
                            order.save()
                        else:
                            order = Sub(name=food, quantity=quantity, size=size, specialInstructions=specialInstructions, user=user, price=7.95)
                            order.save()
                    if name=='Turkey':
                        if size == 'small':
                            order = Sub(name=food, quantity=quantity, size=size, specialInstructions=specialInstructions, user=user, price=7.50)
                            order.save()
                        else:
                            order = Sub(name=food, quantity=quantity, size=size, specialInstructions=specialInstructions, user=user, price=8.50)
                            order.save()
                    if name=='Tuna':
                        if size == 'small':
                            order = Sub(name=food, quantity=quantity, size=size, specialInstructions=specialInstructions, user=user, price=6.50)
                            order.save()
                        else:
                            order = Sub(name=food, quantity=quantity, size=size, specialInstructions=specialInstructions, user=user, price=7.95)
                            order.save()
            except Sub.DoesNotExist:
                try:
                    pasta = Pasta.objects.get(pk=food_id)
                    if isinstance(pasta, Pasta):

                        quantity = int(request.POST["quantity"])
                        sub1_id = request.POST["sub1"] # kad se radi o ForeignKey property klase, mora ici po id jer ForeignKey je uvijek ID!!!
                        sub1 = Sub.objects.get(pk=sub1_id)
                        print("sub1:", sub1)
                        specialInstructions = request.POST["specialInstructions"]
                        order = Pasta(name=food, sub1=sub1, quantity=quantity, specialInstructions=specialInstructions, user=user)
                        order.save()
                except Pasta.DoesNotExist:
                    try:
                        salad = Salad.objects.get(pk=food_id)
                        if isinstance(salad, Salad):
                            quantity = int(request.POST["quantity"])
                            specialInstructions = request.POST["specialInstructions"]
                            order = Salad(name=food, quantity=quantity, specialInstructions=specialInstructions, user=user)
                            order.save()
                    except Salad.DoesNotExist:
                        try:
                            platter = Platter.objects.get(pk=food_id)
                            if isinstance(platter, Platter):
                                quantity = int(request.POST["quantity"])
                                size = request.POST["size"]
                                specialInstructions = request.POST["specialInstructions"]
                                order = Platter(name=food, quantity=quantity, size=size, specialInstructions=specialInstructions, user=user)
                                order.save()
                        except Platter.DoesNotExist:
                            return render(request, "orders/error.html", {"message": "Not a pizza or a topping or a sub or a pasta or a salad or a platter."})
        except KeyError:
            return render(request, "orders/error.html", {"message": "No selection, no id."})
    return HttpResponseRedirect(reverse("orders"))


def card(request, user_id):
    user=request.user
    context = {
        "pizzas": Pizza.objects.filter(user=user).all(),
        "toppings": Topping.objects.filter(user=user).all(),
        "subs": Sub.objects.filter(user=user).all(),
        "pastas": Pasta.objects.filter(user=user).all(),
        "salads": Salad.objects.filter(user=user).all(),
        "platters": Platter.objects.filter(user=user).all()
    }

    return render(request, "orders/card.html", context)
