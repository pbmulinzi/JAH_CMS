import django_filters
from django_filters import DateFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte') # gte = greater than or equal to)
    end_date = DateFilter(field_name='date_created', lookup_expr='lte') # lte = later than or equal to)
    class Meta:
        model = Order
        fields = ['Product', 'status',]
