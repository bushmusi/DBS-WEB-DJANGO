from django.contrib import admin
from django.urls import include, path 
from django.views.generic.base import TemplateView 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

def home(request):
    form = UserCreationForm()
    return render(request,'layouts/body.html',{'form':form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request,'layouts/body.html',{'form':form})
    else:
        form = UserCreationForm()
    return render(request,'layouts/body.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('signup/')
    else:
        form = AuthenticationForm()
    return render(request,'registration/signup.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('registration/login.html')   

def adminlte(request):
    return render('adminlte') 