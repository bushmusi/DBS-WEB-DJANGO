from django.urls import path

from . import views

app_name='customer'

urlpatterns = [
    path('', views.index, name='index'),
    path('itempost',views.itemPost,name='itemPost')
]