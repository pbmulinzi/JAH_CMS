from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.dashboard, name='home'),
    path('user/', views.userPage, name = 'user-page'),

    path('accountSettings/', views.accountSettings, name = 'accountSettings'),

    path('products/', views.products, name='products'),
    path('customers/<int:cust_id>/', views.customers, name='customers'),

    path('createOrder/<str:pk>/', views.createOrder, name='createOrder'),
    path('updateOrder/<str:pk>/', views.updateOrder, name='updateOrder'),
    path('deleteOrder/<str:pk>/', views.deleteOrder, name='deleteOrder'),
    path('updateCustomer/<str:pk>/', views.updateCustomer, name='updateCustomer'),
    path('createCustomer/', views.createCustomer, name='createCustomer'),


#Troubleshoot: find out why the email isn't arriving!
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'Jah_Accounts/Password_reset.html'), name='reset_password'),

    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'Jah_Accounts/Password_reset_sent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'Jah_Accounts/Password_reset_form.html'), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'Jah_Accounts/Password_reset_complete.html'), name='password_reset_complete'),


]

