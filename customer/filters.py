import django_filters
from django_filters import CharFilter

from restaurant.models import *

class StoreFilter(django_filters.FilterSet):
    #name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Restaurant_Account
        fields = {
            'name': ['icontains'],
            'country': ['icontains'],
        }

class MenuFilter(django_filters.FilterSet):
    item = CharFilter(field_name='item', lookup_expr='icontains')
    class Meta:
        model = Menu
        fields = ['category', 'item', 'price']