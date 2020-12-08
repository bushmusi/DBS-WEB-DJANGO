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
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # temp starts
    path('tempFetch',views.tempFetch,name='tempFetch'),
    # end temp

    path('admin/', admin.site.urls),

    path('', include('django.contrib.auth.urls')),
    path('',views.home,name='home'),
    
    path('signup/', views.signup_view, name='signup'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),

    # Password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/reset_password.html'),
        name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset_password_input.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_complete'),
    # endof pwd reset

    path('customer/', include('customer.urls')),
    path('company/', include('company.urls')),
    path('broker/', include("broker.urls")),
    path('administrator/',include('administrator.urls'))
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
