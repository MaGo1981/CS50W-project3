from django import forms
# from .models import Pasta

class FoodForm(forms.Form):
    quantity = forms.IntegerField(label="Quantity")
    specialInstructions = forms.CharField(max_length=640, label="Special Instructions")


class ToppingForm(forms.FoodForm):
    side = forms.CharField(max_length=64, label="Side")

# class PastaForm(forms.ModelForm):
#     class Meta:
#         model = Pasta
#         fields = ["sub1", "specialInstructions", "quantity"]
