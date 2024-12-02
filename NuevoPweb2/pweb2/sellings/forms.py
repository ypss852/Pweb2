from django import forms
from .models import Selling

class SellingForm(forms.ModelForm):
    class Meta:
        model = Selling
        fields = ['product', 'quantity', 'total_price']
