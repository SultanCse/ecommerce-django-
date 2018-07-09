from django.shortcuts import render, redirect
from user.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register(request):
    form = RegisterForm(request.POST or None)
    context={
        'form' : form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        instance = User.objects.create_user(
            username = username,
            email = email,
            password = password,
            first_name = first_name,
            last_name = last_name,
            is_active = True,
            is_staff = False,
            is_superuser = False
        )
        return redirect('/')
    return render(request, 'user/register.html', context)

def login_fun(request):
    form = LoginForm(request.POST or None)
    context = {
        'form' : form,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')        
    return render(request, 'user/login.html', context)

def logout_fun(request):
    logout(request)
    return redirect('/') 