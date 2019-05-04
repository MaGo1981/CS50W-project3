from django import forms
from orders.models import Beverage

class BeverageForm(forms.ModelForm):
    name = forms.CharField(max_length=64, default='Coca-Cola')
    size = forms.CharField(max_length=64, default='2 dl')
    quantity = forms.IntegerField(default=1)
    specialInstructions = forms.CharField(max_length=640, default='No special instructions')

    class meta:
        model = Beverage
        fields = ("name", "size", "quantity", "specialInstructions")
