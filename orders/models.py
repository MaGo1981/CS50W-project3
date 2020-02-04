from django.db import models
from django.contrib.auth.models import User
import datetime

class FoodPrice(models.Model):
	_name = models.CharField(max_length=64, default='FoodPrice')
	_smallRegular = models.FloatField(default=5)
	_largeRegular = models.FloatField(default=10)

	# def getPrice(self):
	# 	return self._smallRegular

	def __str__(self):
		return f"{self._name} "


class PizzaPrice(FoodPrice):
	_small1topping = models.FloatField(default=6)
	_large1topping = models.FloatField(default=11)
	_small2toppings = models.FloatField(default=7)
	_large2toppings = models.FloatField(default=12)
	_small3toppings = models.FloatField(default=8)
	_large3toppings = models.FloatField(default=13)
	_smallSpecial = models.FloatField(default=9)
	_largeSpecial = models.FloatField(default=14)






class NewFood(models.Model):
	"""
    A simple food class
    """

	_name = models.CharField(max_length=64, default='Regular Pizza')
	_specialInstructions = None
	_menuPosition = models.FloatField(default=1)


	def setSpecialInstructions(self,specialInstructions):
		self._specialInstructions = specialInstructions


	def __str__(self):
		if self._specialInstructions != None:
			return f"{self._name}, special instructions: {self._specialInstructions} "
		else:
			return f"{self._name}"


class NewTopping(NewFood):
	"""
	A simple topping class
	"""
	_side = models.CharField(max_length=64, default='whole')




	def __str__(self):
		if self._specialInstructions != None:
			return f"{self._name} side: {self._side}  special instructions: {self._specialInstructions} "
		else:
			return f"{self._name} side: {self._side} "



class NewPizza(NewFood):
	"""A simple pizza class"""

	_topping1 = models.ForeignKey(NewTopping, on_delete=models.CASCADE, related_name="topping1", null=True, blank=True)
	_topping2 = models.ForeignKey(NewTopping, on_delete=models.CASCADE, related_name="topping2", null=True, blank=True)
	_topping3 = models.ForeignKey(NewTopping, on_delete=models.CASCADE, related_name="topping3", null=True, blank=True)


	def setPizzaPriceAndTotal(self, pizzaPrice):
		if self._size == 'large' and self._food._specialInstructions != None:
			self._price = pizzaPrice._largeSpecial
		elif self._size == 'small' and self._food._specialInstructions != None:
			self._price = pizzaPrice._smallSpecial
		elif self._size == 'large' and self._food._topping3 != None:
			self._price = pizzaPrice._large3toppings
		elif self._size == 'small' and self._food._topping3 != None:
			self._price = pizzaPrice._small3toppings
		elif self._size == 'large' and self._food._topping2 != None:
			self._price = pizzaPrice._large2toppings
		elif self._size == 'small' and self._food._topping2 != None:
			self._price = pizzaPrice._small2toppings
		elif self._size == 'large' and self._food._topping1 != None:
			self._price = pizzaPrice._large1toppings
		elif self._size == 'small' and self._food._topping1 != None:
			self._price = pizzaPrice._small1toppings
		elif self._size == 'large' and self._food._topping1 == None:
			self._price = pizzaPrice._largeRegular
		else:
			self._price = pizzaPrice._smallRegular
		self._total = self._price*self._quantity


	def __str__(self):
		if self._topping1 != None and self._specialInstructions != None and self._topping2 == None and self._topping3 == None:
			return f"{self._name} topping1: {self._topping1._name} \
			special instructions: {self._specialInstructions} "
		elif self._topping1 != None and self._specialInstructions == None and self._topping2 == None and self._topping3 == None:
			return f"{self._name} topping1: {self._topping1._name}"
		elif self._topping1 != None and self._specialInstructions == None and self._topping2 != None and self._topping3 == None:
			return f"{self._name} topping1: {self._topping1._name} topping2: {self._topping2._name}"
		elif self._topping1 != None and self._specialInstructions != None and self._topping2 != None and self._topping3 == None:
			return f"{self._name} topping1: {self._topping1._name} topping2: {self._topping2._name}\
			special instructions: {self._specialInstructions} "
		elif self._topping1 != None and self._specialInstructions == None and self._topping2 != None and self._topping3 != None:
			return f"{self._name} topping1: {self._topping1._name} topping2: {self._topping2._name}\
			 topping3: {self._topping3._name}"
		elif self._topping1 != None and self._specialInstructions != None and self._topping2 != None and self._topping3 != None:
			return f"{self._name} topping1: {self._topping1._name} topping2: {self._topping2._name}\
			topping3: {self._topping3._name} special instructions: {self._specialInstructions} "
		else:
			return f"{self._name} "

class NewSalad(NewFood):


	def __str__(self):
		if self._specialInstructions != None:
			return f"{self._name}, special instructions: {self._specialInstructions} "
		else:
			return f"{self._name}"


class Item(models.Model):
	_food = models.ForeignKey(NewFood, on_delete=models.CASCADE) # None limit_choices_to={'is_staff': True},
	_size = models.CharField(max_length=64, default='small')
	_quantity = models.IntegerField(default=1)
	_price = models.ForeignKey(FoodPrice, on_delete=models.CASCADE, null=True, blank=True) # None
	_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="itemUser", default=1)
	_menu = models.BooleanField(default=False)
	# _order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")

	def getFoodFromItem(self):
		return self._food

	def getFoodPosition():
		return '_food___menuPosition' # extra dunder between fields for order_by() function argument


	def setPriceAndTotal(self, priceClass): # filter priceClass by self_name = priceClass_name
		if self._size == 'large':
			self._price = price._largeRegular
		elif self._size == 'small':
			self._price = price._smallRegular
		self._total = self._price*self._quantity


	def getName(self):
		return self._food._name

	def getPrice(self):
		return self._price._smallRegular

	def setPizzaItemPriceAndTotal(self):
		if isinstance(self._food, NewPizza):
			if self._size == 'large' and self._food._specialInstructions != None:
				self._price = pizzaPrice._largeSpecial
			elif self._size == 'small' and self._food._specialInstructions != None:
				self._price = pizzaPrice._smallSpecial
			elif self._size == 'large' and self._food._topping3 != None:
				self._price = pizzaPrice._large3toppings
			elif self._size == 'small' and self._food._topping3 != None:
				self._price = pizzaPrice._small3toppings
			elif self._size == 'large' and self._food._topping2 != None:
				self._price = pizzaPrice._large2toppings
			elif self._size == 'small' and self._food._topping2 != None:
				self._price = pizzaPrice._small2toppings
			elif self._size == 'large' and self._food._topping1 != None:
				self._price = pizzaPrice._large1toppings
			elif self._size == 'small' and self._food._topping1 != None:
				self._price = pizzaPrice._small1toppings
			elif self._size == 'large' and self._food._topping1 == None:
				self._price = pizzaPrice._largeRegular
			else:
				self._price = pizzaPrice._smallRegular
			self._total = self._price*self._quantity

	def __str__(self):
		return f"{self._food}, quantity: {self._quantity}, price: {self.getPrice()}, size: {self._size}"

class Order(models.Model):
	_items = models.ManyToManyField(Item, related_name="items") # filter items by user
	_created = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") #models.DateTimeField(auto_now_add=True)
	_status = models.CharField(max_length=64, default='Open')

	def closeOrder(self, newstatus="Closed"):
		self._status = newstatus

	def getItems(self):
		return self._items

	# def getUser(self):
	# 	return "User:" + self._user

	def getDT(self):
		return "Date & Time:" + self._created


	def __str__(self):
	    return f"items: {'-'.join([str(item) for item in self._items.all()])}, date and time: {self.getDT()}"

		# user: {self.getUser()},






















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
