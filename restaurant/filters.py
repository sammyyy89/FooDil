import django_filters
from django_filters import CharFilter

from .models import *

class MenuFilter(django_filters.FilterSet):
    item = CharFilter(field_name='item', lookup_expr='icontains')
    class Meta:
        model = Menu
        fields = ['category', 'item', 'price']