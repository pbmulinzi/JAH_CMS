from django.shortcuts import render
from .models import *

# Create your views here.

def dashboard(request):

    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    pending = Order.objects.filter(status = 'Pending').count()
    delivered = Order.objects.filter(status = 'Delivered').count()

    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'pending': pending, 'delivered': delivered,}
    return render(request, 'Jah_Accounts/Dashboard.html', context)

def products(request):

    products = Product.objects.all()
    return render(request, 'Jah_Accounts/Products.html', {'products': products})

def customers(request):

    customers = Customer.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()

    customer_products_orders = {'customers': customers, 'products': products, 'orders': orders,}
    return render(request, 'Jah_Accounts/Customer.html', customer_products_orders)