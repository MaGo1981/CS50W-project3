
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
