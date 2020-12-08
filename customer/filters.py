import django_filters
from django_filters import NumberFilter

from .models import *


class ItemPostFilter(django_filters.FilterSet):
    min_price = NumberFilter(field_name='item_price',lookup_expr='gte', label="Maximum price")
    max_price = NumberFilter(field_name='item_price',lookup_expr='lte',  label="Minimum price")

    class Meta:
        model = ItemPost
        fields = "__all__"
        exclude = ['user_id', 'availabilty',
                   'item_type', 'item_price', 'serviceType']
