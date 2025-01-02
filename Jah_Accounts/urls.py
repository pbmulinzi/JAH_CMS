from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('products/', views.products, name='products'),
    path('customers/<cust_id>/', views.customers, name='customers'),

    path('createOrder/', views.createOrder, name='createOrder'),
    path('updateOrder/<str:pk>/', views.updateOrder, name='updateOrder'),
]

