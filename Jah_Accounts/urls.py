from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.dashboard, name='home'),
    path('products/', views.products, name='products'),
    path('customers/<cust_id>/', views.customers, name='customers'),

    path('createOrder/<str:pk>/', views.createOrder, name='createOrder'),
    path('updateOrder/<str:pk>/', views.updateOrder, name='updateOrder'),
    path('deleteOrder/<str:pk>/', views.deleteOrder, name='deleteOrder'),
    path('updateCustomer/<str:pk>/', views.updateCustomer, name='updateCustomer'),
    path('createCustomer/', views.createCustomer, name='createCustomer'),
]

