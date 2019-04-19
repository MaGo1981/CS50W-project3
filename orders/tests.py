from django.test import Client, TestCase
from django.db.models import Max

from .models import Food, Topping, Pizza
from django.contrib.auth.models import User

# Create your tests here.
class PizzaTestCase(TestCase):

    def setUp(self):

        # Create toppings.
        u1 = User.objects.create(first_name="Marko")

        # Create toppings.
        t1 = Topping.objects.create(name="Oregano", side="whole", user=u1)
        t2 = Topping.objects.create(name="Oregano", side="left", user=u1)
        t3 = Topping.objects.create(name="Oregano", side="right", user=u1)
        t4 = Topping.objects.create(name="Onions", side="whole", user=u1)
        t5 = Topping.objects.create(name="Onions", side="left", user=u1)
        t6 = Topping.objects.create(name="Onions", side="right", user=u1)
        t7 = Topping.objects.create(name="Olives", side="whole", user=u1)
        t8 = Topping.objects.create(name="Olives", side="left", user=u1)
        t9 = Topping.objects.create(name="Olives", side="right", user=u1)

        # Create pizzas.
        Pizza.objects.create(topping1=t1, topping2=t2, topping3=t3, user=u1)
        Pizza.objects.create(topping1=t1, topping2=t5, topping3=t9, user=u1)

    # TESTING THE BACKEND SIDE - DATABASE, MODELS, METHODS ETC.

    def test1_validPizza(self):
        a1 = Topping.objects.get(name="Oregano",side="whole")
        a2 = Topping.objects.get(name="Onions",side="left")
        a3 = Topping.objects.get(name="Olives",side="right")
        p = Pizza.objects.get(topping1=a1, topping2=a2, topping3=a3)
        self.assertTrue(p.is_valid_pizza())

    def test2_validPizza(self):
        a1 = Topping.objects.get(name="Oregano",side="whole")
        a2 = Topping.objects.get(name="Oregano",side="left")
        a3 = Topping.objects.get(name="Oregano",side="right")
        p = Pizza.objects.get(topping1=a1, topping2=a2, topping3=a3)
        self.assertFalse(Pizza.is_valid_pizza(p))

    # TESTING THE TEMPLATE SIDE - RESPONSES CODES, CONTEXT, ETC.

    def test_menu(self):
        c = Client()
        response = c.get("menu")
        self.assertEqual(response.status_code, 200) # AssertionError: 404 != 200; 404 Not found
        self.assertEqual(response.context["pizzas"].count(), 2)

    def test_valid_food_page(self):
        a1 = Topping.objects.get(name="Oregano",side="whole")
        a2 = Topping.objects.get(name="Onions",side="left")
        a3 = Topping.objects.get(name="Olives",side="right")
        p = Pizza.objects.get(topping1=a1, topping2=a2, topping3=a3)
        food_id=p.id
        # print(p)
        # print(p.id)
        # print(food_id)
        c = Client()
        # print(c)
        # response = c.get(f"/{p.id}") # with this code it returnes ERROR django.urls.exceptions.NoReverseMatch: Reverse for 'card' with arguments '(None,)' not found. 1 pattern(s) tried: ['(?P<user_id>[0-9]+)/card$']
        response = c.get(food_id)
        # print(response)
        self.assertEqual(response.status_code, 200)
