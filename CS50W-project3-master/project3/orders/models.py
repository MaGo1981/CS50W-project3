from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=64, default='Dirt')

    def __str__(self):
        return f"{self.name}"


class Topping(Food):
    side = models.CharField(max_length=64, default='whole')

    def __str__(self):
        return f"{self.name} - {self.side}"

class Pizza(Food):
    size = models.CharField(max_length=64, default='small')
    topping1 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="topping1")
    topping2 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="topping2")
    topping3 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="topping3")

    def __str__(self):
        return f"{self.name} - {self.size}, with toppings:{self.topping1}, {self.topping2}, {self.topping3}"
'''
Using:
first create instances of class Topping, then create instances of class Pizza
from orders.models import Food, Pizza, Topping
t1=Topping(name='ham')
p1=Pizza(name='Regular', topping1=t1, topping2=t1, topping3=t1)
p1
<Pizza: Regular with toppings ham , ham , ham >
'''
