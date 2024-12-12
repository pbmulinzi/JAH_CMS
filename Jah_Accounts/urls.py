from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('products/', views.products),
    path('customers/<str:pk_test>/', views.customers),
]

