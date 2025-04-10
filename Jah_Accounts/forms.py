from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

from .models import *

#creating/ updating an order
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

##creating/ updating a customer
class AccountCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['user', 'name', 'phone', 'email']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class CreateCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'user']

#form for user registration
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']