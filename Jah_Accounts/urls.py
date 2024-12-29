from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('products/', views.products, name='products'),
    path('customers/<pk_test>/', views.customers, name='customers'),
]

