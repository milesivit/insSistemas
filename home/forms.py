from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label="Username",
        widget= forms.TextInput(
            attrs={'class':'form-control'}
        )
    ) 
    password1 = forms.CharField(
        max_length=150,
        label="Password",
        widget= forms.PasswordInput(
            attrs={'class':'form-control'}
        )
    ) 
    password2 = forms.CharField(
        max_length=150,
        label="Repeat your password",
        widget= forms.PasswordInput(
            attrs={'class':'form-control'}
        )
    ) 
    email = forms.EmailField(
        label="Email",
        widget= forms.EmailInput(
            attrs={'class':'form-control'}
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya fue utilizado")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email de usuario ya fue utilizado")
        return email

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get("password1")
        pass2 = cleaned_data.get("password2")

        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError("Las contraseñas no coinciden")

class LoginForm(forms.Form):
    username=forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
            }
        )
    )
    password=forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )