from django import forms

class FoodForm(forms.Form):
    quantity = forms.IntegerField(label="Quantity")
    specialInstructions = forms.CharField(max_length=640, label="Special Instructions")


class ToppingForm(FoodForm):
    side = forms.CharField(max_length=64, label="Side")
