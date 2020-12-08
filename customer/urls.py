from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name='customer'

urlpatterns = [
    # trila line of code
    # temp map file
    # path('map/',views.default_map,name='map'),

    # end temp

    path('', views.index, name='index'),
    path('submitWishList',views.submitWishList,name='submitWishList'),
    # done by biniam
    path('car/',views.carIndexView,name='car'),
    path('house/',views.houseIndexView,name='house'),
    # end done by biniam
    path('carItemPost/',views.carItemPostView,name='carItemPost'),
    path('houseItemPost/',views.houseItemPostView,name='houseItemPost'),
    path('fetchTemp/',views.fetchTempView.as_view()),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)