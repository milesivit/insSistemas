from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.views import View
from home.forms import LoginForm, RegisterForm
from django.template.loader import render_to_string

# Traduccion
from django.utils.translation import activate, get_language, deactivate

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class Registerview(View):
    def get(self, request):
        form = RegisterForm()
        return render(
            request,
            'accounts/register.html',
            {"form": form}
        )
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )

            subject = "Registro existoso"
            message = render_to_string(
                'mails/welcome.html',
                {'email':user.email}
            )
            email= EmailMessage(
                subject=subject,
                body=message,
                from_email= settings.EMAIL_HOST_USER,
                to=[user.email]        
            )
            email.send()

            messages.success(
                request,
                "Successfully registered user"
            )
        return render(
            request,
            'accounts/register.html',
            {"form" : form }
        )
    
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(
            request,
            'accounts/login.html',
            {"form": form}
        )

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request, 
                username=username, 
                password=password
            )

            if user is not None: 
                login(request, user)
                messages.success(request, "Session started")
                return redirect("index")
            else:
                messages.error(request, "The username or password does not match")
                
        return render(
            request, 
            "accounts/login.html", 
            {'form': form}
        ) 