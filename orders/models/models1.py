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
    status = models.CharField(max_length=64, default='Pending...')

    def get_priceSmallSubtotal(self):
        return round((round((self.priceSmall),2) * self.quantity),2 )

    def get_priceLargeSubtotal(self):
        return round((round((self.priceLarge),2) * self.quantity),2 )

    def set_Status(self, newstatus="Completed"):
        self.status = newstatus

    def __str__(self):
        return f"{self.name}"


class Topping(Food):
    side = models.CharField(max_length=64, default='whole')

    def __str__(self):
        return f"{self.name} - {self.side}, special instructions: {self.specialInstructions}, quantity: {self.quantity}"


class Pizza(Food):
    size = models.CharField(max_length=64, default='small')
    topping1 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="topping1", null=True, blank=True)
    topping2 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="topping2", null=True, blank=True)
    topping3 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="topping3", null=True, blank=True)

# dodaj is_validPizza metodu koja provjerava da li se toppings preklapaju! Testiraj!
    # def is_valid_flight(self):
    #     return (self.origin != self.destination) and (self.duration >= 0)

    def is_valid_pizza(self):
        if (self.topping1.name != "None") and (self.topping2.name != "None") and (self.topping3.name != "None"):
            return (self.topping1.name != self.topping2.name) and (self.topping1.name != self.topping3.name) and (self.topping2.name != self.topping3.name)
        elif (self.topping1.name == "None") and (self.topping2.name == "None") and (self.topping3.name == "None"):
            return True
        elif (self.topping1.name == "None"):
            return self.topping2.name != self.topping3.name
        elif (self.topping2.name == "None"):
            return self.topping1.name == self.topping3.name
        else:
            return self.topping2.name != self.topping3.name


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
            return f"{self.name} Pizza - {self.size}, with toppings:{self.topping1.name}, {self.topping2.name}, {self.topping3.name},  special instructions: {self.specialInstructions}, quantity: {self.quantity}" #{self.priceSmall} eur,, menu item: {self.menu}
        if self.size == 'large':
            return f"{self.name} Pizza - {self.size}, with toppings:{self.topping1.name}, {self.topping2.name}, {self.topping3.name},  special instructions: {self.specialInstructions}, quantity: {self.quantity}" #{self.priceLarge} eur,, menu item: {self.menu}

class Sub(Food):
    size = models.CharField(max_length=64, default='small')

    def __str__(self):
        return f"{self.name} - {self.size}, special instructions: {self.specialInstructions}, quantity: {self.quantity}"


class Pasta(Food):
    sub1 = models.ForeignKey(Sub, on_delete=models.CASCADE, related_name="sub1")


    def __str__(self):
        return f"{self.name} with {self.sub1.name}, special instructions: {self.specialInstructions}, quantity: {self.quantity}"

class Salad(Food):


    def __str__(self):
        return f"{self.name}, special instructions: {self.specialInstructions}, quantity: {self.quantity}"

class Platter(Food):
    size = models.CharField(max_length=64, default='small')

    def __str__(self):
        return f"{self.name} - {self.size}, special instructions: {self.specialInstructions}, quantity: {self.quantity}"
