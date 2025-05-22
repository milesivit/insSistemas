from django import forms

from product.models import Product, Order, OrderDetail

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

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer']

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['order','product', 'quantity']

        widgets = {
            'order': forms.HiddenInput(),
            'product': forms.Select(
                attrs={'class': 'form-control w-50'}
            ),
            'quantity': forms.NumberInput(
                attrs={'class': 'form-control w-25'}
            )
        }

        