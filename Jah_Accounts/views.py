from django.shortcuts import render
from .models import *

# Create your views here.

def dashboard(request):

    orders = Order.objects.all()
    customers = Customer.objects.all()

    customer_n_phones = {'orders': orders, 'customers': customers}
    return render(request, 'Jah_Accounts/Dashboard.html', customer_n_phones)

def products(request):

    products = Product.objects.all()
    return render(request, 'Jah_Accounts/Products.html', {'products': products})

def customers(request):

    customers = Customer.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()

    customer_products_orders = {'customers': customers, 'products': products, 'orders': orders,}
    return render(request, 'Jah_Accounts/Customer.html', customer_products_orders)