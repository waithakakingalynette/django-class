from django import forms
from .models import Product

class Product_Upload_Form(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"