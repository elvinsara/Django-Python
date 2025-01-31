from django import forms
from . models import FoodItems

class ItemForm(forms.ModelForm):
    class Meta:
        model = FoodItems
        fields = ['item_name','item_price','item_desc','item_image']