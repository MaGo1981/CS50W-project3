from django import forms
# from .models import Pasta

SIDE_CHOICES = [
    ('whole', 'Whole'),
    ('left', 'Left'),
    ('right', 'Right')


class FoodForm(forms.Form):
    quantity = forms.IntegerField(label="Quantity")
    specialInstructions = forms.CharField(max_length=640, label="Special Instructions")


class ToppingForm(FoodForm):
    # side = forms.CharField(max_length=64, label="Side")
    side = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=SIDE_CHOICES,
        label="Side"
    )



# class PastaForm(forms.ModelForm):
#     class Meta:
#         model = Pasta
#         fields = ["sub1", "specialInstructions", "quantity"]
