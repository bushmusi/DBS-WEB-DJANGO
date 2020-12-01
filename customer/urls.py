from django.urls import path

from . import views

app_name='customer'

urlpatterns = [
    # trila line of code


    path('', views.index, name='index'),
    path('carItemPost/',views.carItemPostView,name='carItemPost'),
    path('houseItemPost/',views.houseItemPostView,name='houseItemPost')
]