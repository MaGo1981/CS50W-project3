from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FoodSerializer, ToppingsSerializer, PizzasSerializer

from rest_framework.generics import GenericAPIView

from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Food, Pizza, Topping, Sub, Pasta, Salad, Platter

class FoodView(APIView):
    def get(self, request):
        food = Food.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = FoodSerializer(food, many=True)
        return Response({"food": serializer.data})

    def post(self, request):
        food = request.data.get('food')

        # Create food from the above data
        serializer = FoodSerializer(data=food)
        if serializer.is_valid(raise_exception=True):
            food_saved = serializer.save()
        return Response({"success": "Food '{}' created successfully".format(food_saved.name)})

class ToppingsView(APIView):
    def get(self, request):
        toppings = Topping.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ToppingsSerializer(toppings, many=True)
        return Response({"toppings": serializer.data})

    def post(self, request):
        toppings = request.data.get('toppings')

        # Create food from the above data
        serializer = ToppingsSerializer(data=toppings)
        if serializer.is_valid(raise_exception=True):
            topping_saved = serializer.save()
        return Response({"success": "Topping '{}' created successfully".format(topping_saved.name)})

class PizzasView(ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzasSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data.get('user'))
        # topping1 = get_object_or_404(Topping, name=self.request.data.get('topping1'))
        return serializer.save(user=user)

class SinglePizzaView(RetrieveUpdateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzasSerializer
