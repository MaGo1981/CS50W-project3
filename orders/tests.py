from django.test import TestCase, Client
from django.contrib.auth.models import User

from .models import Food, Topping, Pizza

from django.db.models import Max



# Create your tests here.
class ModelTestCase(TestCase):

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
        t10 = Topping.objects.create(name="Onions", side="whole", menu=True)
        t11 = Topping.objects.create(name="Onions", side="left", menu=True)
        t12 = Topping.objects.create(name="Onions", side="right", menu=True)

        # Create user.
        u1 = User.objects.create_user(first_name="Marko", username='admin', email='marko@mail.com', password='admin')

        # Create pizzas.
        p1 = Pizza.objects.create(topping1=t1, topping2=t2, topping3=t3)
        p2 = Pizza.objects.create(topping1=t1, topping2=t5, topping3=t9)
        p3 = Pizza.objects.create(topping1=t1, topping2=t2, topping3=t6, menu=True)


    def test1ValidPizza(self):
        a1 = Topping.objects.get(name="Oregano",side="whole", menu=False)
        a2 = Topping.objects.get(name="Onions",side="left", menu=False)
        a3 = Topping.objects.get(name="Olives",side="right", menu=False)
        p = Pizza.objects.get(topping1=a1, topping2=a2, topping3=a3)
        self.assertTrue(p.is_valid_pizza())

    def testInvalidPizzaToppings(self):
        a1 = Topping.objects.get(name="Oregano",side="whole")
        a2 = Topping.objects.get(name="Oregano",side="left")
        a3 = Topping.objects.get(name="Oregano",side="right")
        p = Pizza.objects.get(topping1=a1, topping2=a2, topping3=a3)
        self.assertFalse(Pizza.is_valid_pizza(p))

    def testToppingsNameCount(self):
        t = Topping.objects.filter(name="Onions")
        self.assertEqual(t.count(), 6)

    def testToppingsNamesCount(self):
        t = Topping.objects.exclude(name="Oregano")
        self.assertEqual(t.count(), 9)

    def testIndex(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)

    def testLoginCredentialsOk(self):
        c = Client()
        response = c.post('/login', {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 302)

    def testLoginCredentialsNotOk(self):
        c = Client()
        response = c.post('/login', {'username': 'admin', 'password': 'wrong'})
        self.assertEqual(response.status_code, 200)

    def testMenuPage(self):
        c = Client()
        response = c.post('/login', {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 302)

        response = c.get("/menu")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["pizzas"].count(), 1)
        self.assertEqual(response.context["toppings"].count(), 3)

    def testFoodPage(self):
        c = Client()
        response = c.post('/login', {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 302)

        response = c.get("/food/12")
        self.assertEqual(response.status_code, 200)



    def testFoodPageNotFound(self):
        c = Client()
        response = c.post('/login', {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 302)

        max_id = Food.objects.all().aggregate(Max("id"))["id__max"]
        response = c.get(f"food/{max_id + 1}")
        self.assertEqual(response.status_code, 404)
