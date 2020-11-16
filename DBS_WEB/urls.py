"""DBS_WEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView 
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/',views.logout_view,name='logout'),

    path('customer/', include('customer.urls')),
    path('company/', include('company.urls')),
    path('broker/', include("broker.urls")),
    path('administrator/',include('administrator.urls'))
]
