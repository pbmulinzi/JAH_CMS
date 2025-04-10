from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import HttpResponse

from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

import logging

logger = logging.getLogger(__name__)

'''
@unauthenticated_user
@csrf_protect
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            logger.info(f'User created: {username}')

            Customer.objects.create(user=user, name= username)        
            logger.info(f'Customer created for user: {username}')


            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        else:
            messages.info(request, 'Try again.')
            logger.warning(f'Form errors: {form.errors}')

    context = {'form': form}
    return render(request, 'Jah_Accounts/register.html', context)

'''


@unauthenticated_user
#@csrf_protect
def registerPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            #Create a customer object for the new user
            Customer.objects.create(user=user)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        else:
            messages.info(request, 'Try again.')


    context = {'form': form}
    return render(request, 'Jah_Accounts/register.html', context)



@unauthenticated_user
#@csrf_protect
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect.')

    context = {}
    return render(request, 'Jah_Accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
#@admin_only
def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    # pending = Order.objects.filter(status__startswith='P').count()
    pending = Order.objects.filter(status = "Pending").count()
    delivered = Order.objects.filter(status='Delivered').count()
    out_for_delivery = Order.objects.filter(status='Out for delivery').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'pending': pending,
        'delivered': delivered,
        'out_for_delivery': out_for_delivery,
    }
    return render(request, 'Jah_Accounts/Dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer', 'admin'])
def userPage(request):
    customer, created = Customer.objects.get_or_create(user=request.user)
    orders = customer.order_set.all()

    total_orders = orders.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()
    out_for_delivery = orders.filter(status='Out for delivery').count()

    context = {
        'customer': customer, 
        'orders': orders,
        'total_orders': total_orders,
        'pending': pending,
        'delivered': delivered,
        'out_for_delivery': out_for_delivery,
    }
    return render(request, 'Jah_Accounts/user.html', context)


@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin', 'customer'])
def products(request):
    products = Product.objects.all()
    return render(request, 'Jah_Accounts/Products.html', {'products': products})


@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def customers(request, cust_id):
    customer = Customer.objects.get(id=cust_id)
    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
        'myFilter': myFilter,
    }
    return render(request, 'Jah_Accounts/Customer.html', context)


@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
#@csrf_protect
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('Product', 'Quantity', 'note', 'status'), extra=4)
    customer = Customer.objects.get(user_id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'Jah_Accounts/order_form.html', context)


@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
#@csrf_protect
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'Jah_Accounts/updateOrder.html', context)


@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
#@csrf_protect
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'Jah_Accounts/delete.html', context)


@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
#@csrf_protect
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'Jah_Accounts/updateCustomer.html', context)


@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
#@csrf_protect
def createCustomer(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'Jah_Accounts/createCustomer.html', context)


@login_required(login_url='login')
#@allowed_users(allowed_roles=['customer', 'admin'])
#@csrf_protect
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account settings updated successfully!')
            return redirect('accountSettings')

    context = {'form': form}
    return render(request, 'Jah_Accounts/account_settings.html', context)











