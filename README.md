
Web Programming with Django

This is a pizza restaurant online ordering app.

Login page uses Django AuthenticationForm() method.

Register page uses Django UserCreationForm() method.

For the app, I created superclass Food and subclasses for different types of food.

Menu page displays different types of food that are on the menu.

By clicking on the menu items, user can access food page.

From food page you can select different options of a specific food and order the food.

Pasta food page uses Django Forms.

The app is tested inside Django's tests.py, where different food items are tested,
along with the status code response for each request and responses from the database
requested by the controller.

APIs for class Food and class Topping are created using Django REST Framework APIView.
APIs for class Pizza is created using Django REST Framework GenericAPIView.



# Navesti primjere koje si ranije u v1 koristio, koja nacela krse i cime si ih zamijenio u v2 da bude u skladu s nacelima.


Admin can create different food instances, and different price class instances.
By using a ForeignKey, the admin connects a specific food class to a specific price class.
To access different food class functions we use Strategy pattern. ???
Admin can also create item class instances. Item class instance can encapsulate any of the food class instances.
Item class is used instead of the factory function.
All data attributes are accessed trough getter functions.
