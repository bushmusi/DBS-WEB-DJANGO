from django.contrib import admin
from django.urls import include, path 
from django.views.generic.base import TemplateView 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from customer.forms import AccountForm
from customer.models import *
from django.template.loader import render_to_string # new
from django.template import loader
from django.utils.html import strip_tags
from customer.models import *
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from customer.filters import ItemPostFilter
from django.forms import modelformset_factory
#done by biniam
from django.core.mail import send_mail
from django.conf import settings
#end done by biniam

# temp method

def tempFetch(request):
    posts = House.objects.select_related()
    form = UserCreationForm()
    accForm = AccountForm()
    return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm,'posts':posts})


# Home page
def home(request):
    form = UserCreationForm()
    authForm = AuthenticationForm()
    accForm = AccountForm()
    itemList = ItemPost.objects.all()
    myFilter = ItemPostFilter(request.GET, queryset=itemList)
    itemList = myFilter.qs
    page = request.GET.get('page',1)
    paginator = Paginator(itemList,3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm,'posts':posts,'myFilter':myFilter,'authForm':authForm})

# Registraion
def signup_view(request):
    template_name = 'customer/common/sample_email.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        accForm = AccountForm(request.POST)
        authForm = AuthenticationForm()
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
            subject = render_to_string(
                template_name='customer/common/sample_email_subject.txt'
            )
            message = loader.render_to_string(
                template_name='customer/common/sample_email.txt'
            )
            html_message = render_to_string(
                'customer/common/sample_email.html',{'username':username,'email':email}
            )
            email_from= settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, strip_tags(message), email_from,recipient_list,fail_silently=False,html_message=html_message,)
            # end done by biniam

            return redirect('customer:index')
        else:
            return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm})
    else:
        form = UserCreationForm()
    return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm})


def login_view(request):
    form = UserCreationForm()
    accForm = AccountForm()
    authForm = AuthenticationForm()
    itemList = ItemPost.objects.all()
    myFilter = ItemPostFilter(request.GET, queryset=itemList)
    itemList = myFilter.qs
    page = request.GET.get('page',1)
    paginator = Paginator(itemList,3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        authForm = AuthenticationForm(data=request.POST)
        if authForm.is_valid():
            user = authForm.get_user()
            login(request,user)
            # return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm})
            return redirect('customer:index')
        else:
            return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm,'posts':posts,'myFilter':myFilter,'authForm':authForm})
            # return HttpResponse('error msg')
    else:
        authForm = AuthenticationForm()
        accForm = AccountForm()
    # return render(request,'common/user_rightside_nav.html',{'authForm':authForm,'accForm':accForm})
    



def logout_view(request):
    form = UserCreationForm()
    accForm = AccountForm()
    if request.method == 'POST':
        logout(request)
    return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm}) 
 