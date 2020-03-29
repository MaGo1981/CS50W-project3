from django import forms
from .models import Pasta, Item, NewFood, Pizza3, Topping3

class FoodForm(forms.Form):
    quantity = forms.IntegerField(label="Quantity")
    specialInstructions = forms.CharField(max_length=640, label="Special Instructions")


class ToppingForm(FoodForm):
    OPTIONS = (
                ("whole", "whole"),
                ("left", "left"),
                ("right", "right"),
                )
    side = forms.ChoiceField(widget=forms.Select, choices=OPTIONS)
    # side = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)


class PastaForm(forms.ModelForm):
    class Meta:
        model = Pasta
        fields = ["specialInstructions","sub1", "quantity"]


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ["_size", "_quantity"]

class Pizza3Form(forms.ModelForm):

    class Meta:
        model = Pizza3
        fields = ["_name", "toppings"]
