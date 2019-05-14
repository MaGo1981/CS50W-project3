from django import forms

class FoodForm(forms.Form):
    name = forms.CharField(max_length=64, label="Name")
    priceSmall = forms.FloatField(label="Price Small")
    priceLarge = forms.FloatField(label="Price Large")
    quantity = forms.IntegerField(label="Quantity")
    specialInstructions = forms.CharField(max_length=640, label="Special Instructions")
    menu = forms.BooleanField(label="Menu")
    # user = forms.ForeignKey(User, on_delete=forms.CASCADE, related_name="user", label="User")
    status = forms.CharField(max_length=64, label="Status")

class ToppingForm(FoodForm):
    side = forms.CharField(max_length=64, label="Side")
