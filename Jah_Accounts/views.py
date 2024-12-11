from django.shortcuts import render
from .models import *

# Create your views here.

def dashboard(request):
    return render(request, 'Jah_Accounts/Dashboard.html')

def products(request):

    products = Product.objects.all()
    return render(request, 'Jah_Accounts/Products.html', {'products': products})

def customers(request):
    return render(request, 'Jah_Accounts/Customer.html')