from django.contrib import admin
from django.urls import include, path 
from django.views.generic.base import TemplateView 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from customer.forms import AccountForm
from customer.models import Account

#done by biniam
from django.core.mail import send_mail
from django.conf import settings
#end done by biniam

# Home page
def home(request):
    form = UserCreationForm()
    accForm = AccountForm()
    return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm})

# Registraion
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        accForm = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(request, user)
            # get user model id
            uID = User.objects.get(username = username).pk
            # get value from Account model
            aID = Account.objects.get(user = uID)
            # Update the refrenced model
            aID.phone_num = accForm['phone_num'].value()
            # Save the change
            aID.save()
            # done by biniam
            subject = 'welcome to DBS'
            message = 'Hi {user.username}, thank you for registering to Digital Broker System'
            email_from= settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail(subject, message, email_from,recipient_list)
            # end done by biniam
            return redirect('customer:index')
        else:
            return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm})
    else:
        form = UserCreationForm()
    return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm})


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
 