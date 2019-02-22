from django.http import HttpResponse
from django.shortcuts import render


from .models import Food

# Create your views here.
def index(request):
    context = {
        "foods": Food.objects.all()
    }
    return render(request, "orders/index.html", context)
