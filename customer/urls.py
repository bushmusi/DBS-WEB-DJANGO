from django.urls import path

from . import views

app_name='customer'

urlpatterns = [
    # trila line of code


    path('', views.index, name='index'),
    # done by biniam
    path('car/',views.car,name='car'),
    path('house/',views.house,name='house'),
    # end done by biniam
    path('carItemPost/',views.carItemPostView,name='carItemPost'),
    path('houseItemPost/',views.houseItemPostView,name='houseItemPost'),
    path('fetchTemp/',views.fetchTempView.as_view()),
]