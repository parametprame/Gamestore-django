from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here

def homepage(request):

    return render(request, 'nonregister/homepage.html')

def my_login(request):
    context = {}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = "Wrong username or password!!!!!"
            return render(request, 'nonregister/login.html', context=context)
        pass
    else:
        return render(request, 'nonregister/login.html', context=context)

def register(request):
    
    if request.method == 'POST':

        user = User.objects.create_user(
            first_name=request.POST.get('firstname'),
            last_name=request.POST.get('lastname'),
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            email=request.POST.get('email')
        )
        user.save()

        return render(request, 'nonregister/login.html')
    
    
    return render(request, 'nonregister/register.html')


def my_logout(request):
    logout(request)
    return redirect('home')