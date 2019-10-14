from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FoodSerializer, ToppingsSerializer, PizzasSerializer

from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from .models import Food, Pizza, Topping, Sub, Pasta, Salad, Platter

class FoodView(APIView):
    '''
    This is an API view for all Food class objects.
    '''
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
    '''
    This is an API view for Toppings.
    '''
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
    '''
    This is an API view for Pizzas.
    '''
    queryset = Pizza.objects.all()
    serializer_class = PizzasSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data.get('user'))
        # topping1 = get_object_or_404(Topping, name=self.request.data.get('topping1'))
        return serializer.save(user=user)

class SinglePizzaView(RetrieveUpdateAPIView):
    '''
    This is an API view for single Pizza objects.
    '''
    queryset = Pizza.objects.all()
    serializer_class = PizzasSerializer


class PizzasPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class PizzaList(ListAPIView):
    '''
    This is the secound API view for Pizzas.
    '''
    queryset = Pizza.objects.all()
    serializer_class = PizzasSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'name', 'user', 'size')
    search_fields = ('name', 'specialInstructions')
    pagination_class = PizzasPagination
