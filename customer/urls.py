from django.urls import path

from . import views

app_name='customer'

urlpatterns = [
    # trila line of code


    path('', views.index, name='index'),
    path('itempost/',views.itemPostView,name='itempost')
]