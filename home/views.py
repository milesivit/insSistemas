from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render

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
            messages.error(request, "the password dont match")
        
        elif User.objects.filter(username=username).exists():
            messages.error(request, "the user is in use")
        
        else:
            User.objects.create_user(
                username=username,
                password=pass1,
                email=email
            )
        

    return render(
        request=request,
        template_name='accounts/register.html'
        )