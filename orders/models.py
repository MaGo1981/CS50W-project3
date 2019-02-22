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

class Sub(Food):
    size = models.CharField(max_length=64, default='small')

    def __str__(self):
        return f"{self.name} - {self.size}"

class Pasta(Food):
    sub1 = models.ForeignKey(Sub, on_delete=models.CASCADE, related_name="sub1")


    def __str__(self):
        return f"{self.name} with:{self.sub1.name}"

class Salad(Food):


    def __str__(self):
        return f"{self.name} "

class Platters(Food):
    size = models.CharField(max_length=64, default='Antipasto')

    def __str__(self):
        return f"{self.name} - {self.size}"
