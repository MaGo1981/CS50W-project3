from django.test import Client, TestCase
from django.db.models import Max

from .models import Food, Topping, Pizza

# Create your tests here.
class PizzaTestCase(TestCase):

    def setUp(self):

        # Create toppings.
        t1 = Topping.objects.create(name="Oregano", side="whole")
        t2 = Topping.objects.create(name="Oregano", side="left")
        t3 = Topping.objects.create(name="Oregano", side="right")
        t4 = Topping.objects.create(name="Onions", side="whole")
        t5 = Topping.objects.create(name="Onions", side="left")
        t6 = Topping.objects.create(name="Onions", side="right")
        t7 = Topping.objects.create(name="Olives", side="whole")
        t8 = Topping.objects.create(name="Olives", side="left")
        t9 = Topping.objects.create(name="Olives", side="right")

        # Create pizzas.
        Pizza.objects.create(topping1=t1, topping2=t2, topping3=t3)
        Pizza.objects.create(topping1=t1, topping2=t5, topping3=t9)

    # TESTING THE BACKEND SIDE - DATABASE, MODELS, METHODS ETC.

    def test1_validPizza(self):
        a1 = Topping.objects.get(name="Oregano",side="whole")
        a2 = Topping.objects.get(name="Onions",side="left")
        a3 = Topping.objects.get(name="Olives",side="right")
        p = Pizza.objects.get(topping1=a1, topping2=a2, topping3=a3))
        self.assertTrue(p.is_validPizza())

    def test2_validPizza(self):
        a1 = Topping.objects.get(name="Oregano",side="whole")
        a2 = Topping.objects.get(name="Oregano",side="left")
        a3 = Topping.objects.get(name="Oregano",side="right")
        p = Pizza.objects.get(topping1=a1, topping2=a2, topping3=a3))
        self.assertTrue(p.is_validPizza())

    # TESTING THE TEMPLATE SIDE - RESPONSES CODES, CONTEXT, ETC.

    def test_menu(self):
        c = Client()
        response = c.get("/menu")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["pizzas"].count(), 2)

    def test_valid_food_page(self):
        a1 = Topping.objects.get(name="Oregano",side="whole")
        a2 = Topping.objects.get(name="Oregano",side="left")
        a3 = Topping.objects.get(name="Oregano",side="right")
        p = Pizza.objects.get(topping1=a1, topping2=a2, topping3=a3))

        c = Client()
        response = c.get(f"/{p.id}")
        self.assertEqual(response.status_code, 200)


    def test_invalid_food_page(self):
        max_id = Food.objects.all().aggregate(Max("id"))["id__max"] # We want to get the maximum value of any ID of any flight.
                                                                    # We want to test what happends if we go to an ID number that does not exist.
        c = Client()
        response = c.get(f"/{max_id + 1}")
        self.assertEqual(response.status_code, 404)


    # def test_departures_count(self):
    #     a = Airport.objects.get(code="AAA")
    #     self.assertEqual(a.departures.count(), 3)

    #
    # def test_arrivals_count(self):
    #     a = Airport.objects.get(code="AAA")
    #     self.assertEqual(a.arrivals.count(), 1)


    # def test_invalid_flight_destination(self):
    #     a1 = Airport.objects.get(code="AAA")
    #     f = Flight.objects.get(origin=a1, destination=a1)
    #     self.assertFalse(f.is_valid_flight())
    #
    # def test_invalid_flight_duration(self):
    #     a1 = Airport.objects.get(code="AAA")
    #     a2 = Airport.objects.get(code="BBB")
    #     f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
    #     self.assertFalse(f.is_valid_flight())
