from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=64, default='Dirt')
    priceSmall = models.FloatField(default=1000)
    priceLarge = models.FloatField(default=10000)
    quantity = models.IntegerField(default=1)
    specialInstructions = models.CharField(max_length=640, default='No special instructions')
    menu = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", default=1)

    def __str__(self):
        return f"{self.name}"


class Topping(Food):
    side = models.CharField(max_length=64, default='whole')

    def __str__(self):
        return f"{self.name} - {self.side}, {self.priceSmall} eur, special instructions: {self.specialInstructions}, quantity: {self.quantity}, menu item: {self.menu}"


class Pizza(Food):
    size = models.CharField(max_length=64, default='small')
    topping1 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="topping1")
    topping2 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="topping2")
    topping3 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="topping3")

    def get_priceSmallT1(self):
        return round((self.priceSmall*1.1),2)

    def get_priceSmallT1Subtotal(self):
        return round((round((self.priceSmall*1.1),2) * self.quantity),2 )

    def get_priceLargeT1(self):
        return round((self.priceLarge*1.1),2)

    def get_priceLargeT1Subtotal(self):
        return round((round((self.priceLarge*1.1),2) * self.quantity),2 )

    def get_priceSmallT2(self):
        return round((self.priceSmall*1.1*1.1),2)

    def get_priceSmallT2Subtotal(self):
        return round((round((self.priceSmall*1.1*1.1),2) * self.quantity),2 )

    def get_priceLargeT2(self):
        return round((self.priceLarge*1.1*1.1),2)

    def get_priceLargeT2Subtotal(self):
        return round((round((self.priceLarge*1.1*1.1),2) * self.quantity),2 )

    def get_priceSmallT3(self):
        return round((self.priceSmall*1.1*1.1*1.1),2)

    def get_priceSmallT3Subtotal(self):
        return round((round((self.priceSmall*1.1*1.1*1.1),2) * self.quantity),2 )

    def get_priceLargeT3(self):
        return round((self.priceLarge*1.1*1.1*1.1),2)

    def get_priceLargeT3Subtotal(self):
        return round((round((self.priceLarge*1.1*1.1*1.1),2) * self.quantity),2 )

    def get_SIpriceSmall(self):
        return round((self.priceSmall*1.42),2)

    def get_SIpriceSmallSubtotal(self):
        return round((round((self.priceSmall*1.42),2)* self.quantity),2 )

    def get_SIpriceLarge(self):
        return round((self.priceLarge*1.45),2)

    def get_SIpriceLargeSubtotal(self):
        return round((round((self.priceLarge*1.45),2)* self.quantity),2 )


    def __str__(self):
        if self.size == 'small':
            return f"{self.name} Pizza - {self.size}, with toppings:{self.topping1.name}, {self.topping2.name}, {self.topping3.name},  special instructions: {self.specialInstructions}, quantity: {self.quantity}, menu item: {self.menu}" #{self.priceSmall} eur,
        if self.size == 'large':
            return f"{self.name} Pizza - {self.size}, with toppings:{self.topping1.name}, {self.topping2.name}, {self.topping3.name},  special instructions: {self.specialInstructions}, quantity: {self.quantity}, menu item: {self.menu}" #{self.priceLarge} eur,

class Sub(Food):
    size = models.CharField(max_length=64, default='small')

    def __str__(self):
        if self.size == 'small':
            return f"{self.name} - {self.size}, {self.priceSmall} eur, special instructions: {self.specialInstructions}, quantity: {self.quantity}, menu item: {self.menu}"
        if self.size == 'large':
            return f"{self.name} - {self.size}, {self.priceLarge} eur, special instructions: {self.specialInstructions}, quantity: {self.quantity}, menu item: {self.menu}"

class Pasta(Food):
    sub1 = models.ForeignKey(Sub, on_delete=models.CASCADE, related_name="sub1")


    def __str__(self):
        return f"{self.name} with {self.sub1.name}, {self.priceSmall} eur, special instructions: {self.specialInstructions}, quantity: {self.quantity}, menu item: {self.menu}"

class Salad(Food):


    def __str__(self):
        return f"{self.name}, {self.priceSmall} eur, special instructions: {self.specialInstructions}, quantity: {self.quantity}, menu item: {self.menu}"

class Platter(Food):
    size = models.CharField(max_length=64, default='small')

    def __str__(self):
        if self.size == 'small':
            return f"{self.name} - {self.size}, {self.priceSmall} eur, special instructions: {self.specialInstructions}, quantity: {self.quantity}, menu item: {self.menu}"
        if self.size == 'large':
            return f"{self.name} - {self.size}, {self.priceLarge} eur, special instructions: {self.specialInstructions}, quantity: {self.quantity}, menu item: {self.menu}"
