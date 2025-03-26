import django_filters
from django_filters import DateFilter, CharFilter

# from django_filters import FilterSet
from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte') # gte = greater than or equal to)
    end_date = DateFilter(field_name='date_created', lookup_expr='lte') # lte = later than or equal to)
    note = CharFilter(field_name='note', lookup_expr='icontains') #icontains = ignore case sensitivity!
    class Meta:
        model = Order
        fields = ['Product', 'status',]
