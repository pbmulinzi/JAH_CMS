from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.dashboard, name='home'),
    path('user/', views.userPage, name = 'user-page'),

    path('account/', views.accountSettings, name = 'account'),

    path('products/', views.products, name='products'),
    path('customers/<cust_id>/', views.customers, name='customers'),

    path('createOrder/<str:pk>/', views.createOrder, name='createOrder'),
    path('updateOrder/<str:pk>/', views.updateOrder, name='updateOrder'),
    path('deleteOrder/<str:pk>/', views.deleteOrder, name='deleteOrder'),
    path('updateCustomer/<str:pk>/', views.updateCustomer, name='updateCustomer'),
    path('createCustomer/', views.createCustomer, name='createCustomer'),


#Troubleshoot: find out why the email isn't arriving!
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'Jah_Accounts/Password_reset.html'), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'Jah_Accounts/Password_reset_sent.html'), name='password_reset_sent'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'Jah_Accounts/Password_reset_form.html'), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'Jah_Accounts/Password_reset_complete'), name='password_reset_complete'),


]

