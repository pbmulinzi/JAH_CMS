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

def customers(request, pk_test):

    customers = Customer.objects.get(id = pk_test)
    orders = customers.order_set.all()  #need to re-go through the purpose of this when back online!

    context = {'customers': customers, 'orders': orders,}
    return render(request, 'Jah_Accounts/Customer.html', context)