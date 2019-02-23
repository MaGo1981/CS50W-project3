from django.http import HttpResponse
from django.shortcuts import render


from .models import Food, Pizza, Topping, Sub, Pasta, Salad, Platters

# Create your views here.
def index(request):
    context = {
        "foods": Food.objects.all()
    }
    return render(request, "orders/index.html", context)

def menu(request):
    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Topping.objects.all(),
        "subs": Sub.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all(),
        "platters": Platters.objects.all()
    }

    return render(request, "orders/menu.html", context)
