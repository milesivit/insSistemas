from django import forms

from product.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = ['name', 'price', 'stock']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control w-25 personalizado',
                    'placeholder': 'insert product name',
                    'style': 'background: aquamarine'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control w-25 personalizado',
                    'placeholder': 'insert price',
                    'style': 'background: pink'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control w-25 personalizado',
                    'placeholder': 'insert stock',
                    'style': 'background: lightgreen'
                }
            ),
        }