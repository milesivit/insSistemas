from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        pass1= data.get('password1')
        pass2= data.get('password2')
        email= data.get('email')
        print(username, pass1, pass2)

        if not username or not pass1 or not pass2:
            messages.error(request, "no data")
        
        elif pass1 != pass2:
            messages.error(request, "Passwords dont match")
        
        elif User.objects.filter(username=username).exists():
            messages.error(request, "the user is in use")
        
        else:
            user = User.objects.create_user(
                username=username,
                password=pass1,
                email=email
            )
            login(request, user)  #loguea automáticamente
            messages.success(request, "Registration successful")
            return redirect('index')  #redirige a la home
        

    return render(
        request=request,
        template_name='accounts/register.html'
        )

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request, 
            username=username,
            password=password
        )
        if user is not None: #verifica si el usuario esta bien logueado
            login(request, user)
            messages.success(request, 'sesion success')
            return redirect('index')
        else:
            messages.error(request, 'user or password invalid')
        
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'index.html')
