from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import Food, Pizza, Topping, Sub, Pasta, Salad, Platter, Beverage
from .forms import FoodForm


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        return render(request, "orders/login.html", {"message": "Welcome to Marko's Pizza & Subs! Please Login or Register!", 'form':form})

    context = {
        "user": request.user,

    }
    return render(request, "orders/index.html", context)

def menu(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        return render(request, "orders/login.html", {"message": "Welcome to Marko's Pizza & Subs! Please Login or Register!", 'form':form})

    context = {
        "user": request.user,
        "pizzas": Pizza.objects.exclude(menu=False).all(),
        "toppings": Topping.objects.exclude(menu=False).all(),
        "subs": Sub.objects.exclude(menu=False).all(),
        "pastas": Pasta.objects.exclude(menu=False).all(),
        "salads": Salad.objects.exclude(menu=False).all(),
        "platters": Platter.objects.exclude(menu=False).all(),
        "beverages": Beverage.objects.exclude(menu=False).all()
    }

    return render(request, "orders/menu.html", context)

def orders(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        return render(request, "orders/login.html", {"message": "Welcome to Marko's Pizza & Subs! Please Login or Register!", 'form':form})

    context = {
        "pizzas": Pizza.objects.exclude(menu=True).all(),
        "toppings": Topping.objects.exclude(menu=True).all(),
        "subs": Sub.objects.exclude(menu=True).all(),
        "pastas": Pasta.objects.exclude(menu=True).all(),
        "salads": Salad.objects.exclude(menu=True).all(),
        "platters": Platter.objects.exclude(menu=True).all(),
        "beverages": Beverage.objects.exclude(menu=True).all()
    }

    return render(request, "orders/orders.html", context)

def login_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
         # create a form instance and populate it with data from the request:
        form = AuthenticationForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            user = form.get_user()
            login(request, user)
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("index"))
        # if a GET (or any other method) we'll create a blank form
        else:
            return render(request, "orders/login.html", {'form': form, "message": "You did not suceed! Please try again."})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()
    return render(request, 'orders/login.html', {'form': form, "message": "Please login!"})


def logout_view(request):
    logout(request)
    form = AuthenticationForm()
    return render(request, "orders/login.html", {'form': form, "message": "Logged out."})

def register_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
         # create a form instance and populate it with data from the request:
        form = UserCreationForm(request.POST)
        print("form = ", form)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("login"))
        # if a GET (or any other method) we'll create a blank form
        else:
            return render(request, "orders/register.html", {'form': form, "message": "You did not suceed! Please try again."})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserCreationForm()
    return render(request, 'orders/register.html', {'form': form})


def food(request, food_id):
    # print("food function food_id:", food_id)
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        return render(request, "orders/login.html", {"message": "Welcome to Marko's Pizza & Subs! Please Login or Register!", 'form':form})
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
    FoodForm = FoodForm()
    context = {
        "food": food,
        "allToppings": allToppings,
        "pizzas": pizzas,
        "subs": subs,
        "FoodForm": FoodForm
    }
    return render(request, "orders/food.html", context)


def order(request, food_id):
    # print("order function food_id:", food_id)
    food = Food.objects.get(pk=food_id)
    user=request.user
    user_id=request.user.id
    # print("order function food:", food)
    # print(issubclass(Pizza, Food))
    # print(isinstance(food, Pizza)) # vraca False kad narucujem pizzu, a trebalo bi vracati True
    # print(isinstance(pizza, Pizza))
    # print("food.pizza:", food.pizza) #vraca pizzu s menu-a ili vraca gresku ako narucujes topping
    # print("food.topping:", food.topping ) # obrnuto od food.pizza

    try:
        pizza = Pizza.objects.get(pk=food_id)
        if isinstance(pizza, Pizza):
            # topping1_id = int(request.POST["topping-whole"]) # kad se radi o ForeignKey property klase, mora ici po id jer ForeignKey je uvijek ID!!!
            topping1_ids = request.POST.getlist("topping-whole")
            print("topping1_ids", topping1_ids)
            # topping2_id = int(request.POST["topping-left"]) # kad se radi o ForeignKey property klase, mora ici po id jer ForeignKey je uvijek ID!!!
            topping2_ids = request.POST.getlist("topping-left")
            print("topping2_ids", topping2_ids)
            # topping3_id = int(request.POST["topping-right"])# kad se radi o ForeignKey property klase, mora ici po id jer ForeignKey je uvijek ID!!!
            topping3_ids = request.POST.getlist("topping-right")
            print("topping3_ids", topping3_ids)
            allToppings_ids = topping1_ids + topping2_ids + topping3_ids
            print("allToppings_ids", allToppings_ids)
            priceSmall=food.priceSmall
            print('priceSmall 1', priceSmall)
            priceLarge=food.priceLarge
            if len(allToppings_ids) > 3:
                return render(request, "orders/error.html", {"message": "You can choose maximum of 3 toppings. Please try again!"})
            else:

                try:
                    topping3_id = allToppings_ids[2]
                    topping3 = Topping.objects.get(pk=topping3_id)

                except:
                    topping3 = Topping.objects.get(name="None")

                try:
                    topping2_id = allToppings_ids[1]
                    topping2 = Topping.objects.get(pk=topping2_id)

                except:
                    topping2 = Topping.objects.get(name="None")

                try:
                    topping1_id = allToppings_ids[0]
                    topping1 = Topping.objects.get(pk=topping1_id)

                except:
                    topping1 = Topping.objects.get(name="None")

            quantity = int(request.POST["quantity"])
            size = request.POST["size"]
            specialInstructions = request.POST["specialInstructions"]

            # print("order function topping1_id:",topping1_id)
            # print("order function specialInstructions:",specialInstructions)
            # print("order function topping1:",topping1)
            order = Pizza(name=food, topping1=topping1, topping2=topping2, topping3=topping3, quantity=quantity, size=size, specialInstructions=specialInstructions, user=user, priceSmall=priceSmall, priceLarge=priceLarge)
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
                    priceSmall=food.priceSmall
                    priceLarge=food.priceLarge
                    print('sub name', name)
                    order = Sub(name=food, quantity=quantity, size=size, specialInstructions=specialInstructions, user=user, priceSmall=priceSmall, priceLarge=priceLarge)
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
                        priceSmall=food.priceSmall
                        priceLarge=food.priceLarge
                        order = Pasta(name=food, sub1=sub1, quantity=quantity, specialInstructions=specialInstructions, user=user, priceSmall=priceSmall, priceLarge=priceLarge)
                        order.save()
                except Pasta.DoesNotExist:
                    try:
                        salad = Salad.objects.get(pk=food_id)
                        if isinstance(salad, Salad):
                            quantity = int(request.POST["quantity"])
                            specialInstructions = request.POST["specialInstructions"]
                            priceSmall=food.priceSmall
                            priceLarge=food.priceLarge
                            order = Salad(name=food, quantity=quantity, specialInstructions=specialInstructions, user=user, priceSmall=priceSmall, priceLarge=priceLarge)
                            order.save()
                    except Salad.DoesNotExist:
                        try:
                            platter = Platter.objects.get(pk=food_id)
                            if isinstance(platter, Platter):
                                quantity = int(request.POST["quantity"])
                                size = request.POST["size"]
                                specialInstructions = request.POST["specialInstructions"]
                                priceSmall=food.priceSmall
                                priceLarge=food.priceLarge
                                order = Platter(name=food, quantity=quantity, size=size, specialInstructions=specialInstructions, user=user, priceSmall=priceSmall, priceLarge=priceLarge)
                                order.save()
                        except Platter.DoesNotExist:
                            try:
                                beverage = Beverage.objects.get(pk=food_id)
                                if isinstance(beverage, Beverage):
                                    quantity = int(request.POST["quantity"])
                                    size = request.POST["size"]
                                    specialInstructions = request.POST["specialInstructions"]
                                    priceSmall=food.priceSmall
                                    priceLarge=food.priceLarge
                                    order = Beverage(name=food, quantity=quantity, size=size, specialInstructions=specialInstructions, user=user, priceSmall=priceSmall, priceLarge=priceLarge)
                                    order.save()
                            except Beverage.DoesNotExist:
                                return render(request, "orders/error.html", {"message": "Not a pizza or a topping or a sub or a pasta or a salad or a platter or a beverage."})
        except KeyError:
            return render(request, "orders/error.html", {"message": "No selection, no id."})
    return HttpResponseRedirect(reverse("menu"))


def card(request, user_id):
    user=request.user
    pizzas = Pizza.objects.filter(user=user).all()
    print("PIZZAS:", pizzas)
    pizzaSubtotal = 0
    pizzaItemSmallSubtotalT3 = 0
    for pizza in pizzas:
        if pizza.size == "small" and pizza.topping3.name != 'None' and pizza.specialInstructions == '':
            pizzaSubtotal= pizzaSubtotal + (Pizza.get_priceSmallT3Subtotal(pizza)) # USING CLASS TO GET TO THE METHOD!
        elif pizza.size == "small" and pizza.topping2.name != 'None':
            pizzaSubtotal= pizzaSubtotal + (Pizza.get_priceSmallT2Subtotal(pizza)) # USING CLASS TO GET TO THE METHOD!
        elif pizza.size == "small" and pizza.topping1.name != 'None':
            pizzaSubtotal= pizzaSubtotal + (Pizza.get_priceSmallT1Subtotal(pizza)) # USING CLASS TO GET TO THE METHOD!
        elif pizza.size == "small" and pizza.specialInstructions != '': # bug when also toppings clicked!?
            pizzaSubtotal= pizzaSubtotal + (Pizza.get_SIpriceSmallSubtotal(pizza)) # USING CLASS TO GET TO THE METHOD!
        elif pizza.size == "small":
            pizzaSubtotal = pizzaSubtotal + (Pizza.get_priceSmallSubtotal(pizza)) # USING CLASS TO GET TO THE METHOD!
        elif pizza.size == "large" and pizza.topping3.name != 'None':
            pizzaSubtotal= pizzaSubtotal + (Pizza.get_priceLargeT3Subtotal(pizza)) # USING CLASS TO GET TO THE METHOD!
        elif pizza.size == "large" and pizza.topping2.name != 'None':
            pizzaSubtotal= pizzaSubtotal + (Pizza.get_priceLargeT2Subtotal(pizza)) # USING CLASS TO GET TO THE METHOD!
        elif pizza.size == "large" and pizza.topping1.name != 'None':
            pizzaSubtotal= pizzaSubtotal + (Pizza.get_priceLargeT1Subtotal(pizza)) # USING CLASS TO GET TO THE METHOD!
        elif pizza.size == "large" and pizza.specialInstructions != '': # bug when also toppings clicked!?
            pizzaSubtotal= pizzaSubtotal + (Pizza.get_SIpriceLargeSubtotal(pizza)) # USING CLASS TO GET TO THE METHOD!
        else:
            pizzaSubtotal = pizzaSubtotal + (Pizza.get_priceSmallSubtotal(pizza)) # USING CLASS TO GET TO THE METHOD!
    pizzaSubtotal = round(pizzaSubtotal, 2)
    print("pizzaSubtotal:", pizzaSubtotal)

    subs = Sub.objects.filter(user=user).all()
    print("SUBS:", subs)
    subSubtotal = 0
    for sub in subs:
        if sub.size == "small":
            print("SUB:", sub)
            subSubtotal= subSubtotal + sub.priceSmall * sub.quantity
        else:
            subSubtotal= subSubtotal + sub.priceLarge * sub.quantity
    subSubtotal = round(subSubtotal, 2)
    print("subSubtotal:", subSubtotal)

    platters = Platter.objects.filter(user=user).all()
    platterSubtotal = 0
    for platter in platters:
        if platter.size == "small":
            print("platter:", platter)
            platterSubtotal= platterSubtotal + platter.priceSmall * platter.quantity
        else:
            platterSubtotal= platterSubtotal + platter.priceLarge * platter.quantity
    platterSubtotal = round(platterSubtotal, 2)
    print("platterSubtotal:", platterSubtotal)

    toppings = Topping.objects.filter(user=user).all()
    print("toppingS:", toppings)
    toppingSubtotal = 0
    for topping in toppings:
        print("topping:", topping)
        toppingSubtotal= toppingSubtotal + topping.priceSmall * topping.quantity
    toppingSubtotal = round(toppingSubtotal, 2)
    print("toppingSubtotal:", toppingSubtotal)

    pastas = Pasta.objects.filter(user=user).all()
    print("pastaS:", pastas)
    pastaSubtotal = 0
    for pasta in pastas:
        print("pasta:", pasta)
        pastaSubtotal= pastaSubtotal + pasta.priceSmall * pasta.quantity
    pastaSubtotal = round(pastaSubtotal, 2)
    print("pastaSubtotal:", pastaSubtotal)

    salads = Salad.objects.filter(user=user).all()
    print("saladS:", salads)
    saladSubtotal = 0
    for salad in salads:
        print("salad:", salad)
        saladSubtotal= saladSubtotal + salad.priceSmall * salad.quantity
    saladSubtotal = round(saladSubtotal, 2)
    print("saladSubtotal:", saladSubtotal)

    total= pizzaSubtotal+subSubtotal+platterSubtotal+pastaSubtotal+saladSubtotal+toppingSubtotal

    context = {
        "pizzas": Pizza.objects.filter(user=user).all(),
        "toppings": Topping.objects.filter(user=user).all(),
        "subs": Sub.objects.filter(user=user).all(),
        "pastas": Pasta.objects.filter(user=user).all(),
        "salads": Salad.objects.filter(user=user).all(),
        "platters": Platter.objects.filter(user=user).all(),
        "pizzaSubtotal": pizzaSubtotal,
        "subSubtotal": subSubtotal,
        "platterSubtotal": platterSubtotal,
        "pastaSubtotal": pastaSubtotal,
        "saladSubtotal": saladSubtotal,
        "toppingSubtotal": toppingSubtotal,
        # "pizzaItemSubtotal": pizzaItemSubtotal,
        "pizzaItemSmallSubtotalT3": pizzaItemSmallSubtotalT3,
        "total": total
    }
    return render(request, "orders/card.html", context)

def set_Status(request, food_id):
    print("food_id:", food_id)
    food = Food.objects.get(pk=food_id)
    print("food:", food)
    Pizza.set_Status(food, newstatus="Completed")
    print("food.status:", food.status)
    food.save()
    return HttpResponseRedirect(reverse("orders"))



def confirmOrder(request, user_id):
    print("user_id:", user_id)
    user = User.first_name
    # print("user:", user)
    # print("user.status:", user.status)
    return render(request, "orders/confirmation.html", {"message": "Such a thing has never been made. If you survive, please come again!!"})

def addFood(request):
    form = FoodForm(request.POST)
    if form.is_valid():
        food = Food(name = form.cleaned_data["name"],
                    priceSmall = form.cleaned_data["priceSmall"],
                    priceLarge = form.cleaned_data["priceLarge"],
                    quantity = form.cleaned_data["quantity"],
                    specialInstructions = form.cleaned_data["specialInstructions"],
                    menu = form.cleaned_data["menu"],
                    status = form.cleaned_data["status"])
        food.save()
    return HttpResponseRedirect(reverse("orders"))
