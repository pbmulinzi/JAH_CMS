from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group 

from django.contrib import messages


#Create your views here
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only 


@unauthenticated_user
def registerPage(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'customer')
            user.groups.add(group)

            messages.success(request, 'Account was created for '+ username)
            return redirect('login')

    context = {'form': form,}
    return render(request, 'Jah_Accounts/register.html', context)

@unauthenticated_user #defined in the decorators file
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username OR password is incorrect.')

    context = {}
    return render(request, 'Jah_Accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def dashboard(request):

    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    pending = Order.objects.filter(status = 'Pending').count()
    delivered = Order.objects.filter(status = 'Delivered').count()
    Out_for_Delivery =  Order.objects.filter(status = 'Out for delivery').count()


    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'pending': pending, 'delivered': delivered, 'Out_for_Delivery': Out_for_Delivery}
    return render(request, 'Jah_Accounts/Dashboard.html', context)

    # return render(request, 'Jah_Accounts/Dashboard.html', {**context , 'email_address' : email_address})
    #we use double stars for spread operators in dictionaries, and a single star for spread operators in lists
    #THE COMMENTED CODE ABOVE ENTAILS THE USE OF SPREAD OPERATORS, TO BE READ ABOUT.....AS STATED IN THE COMMENTS BELOW. It's been commented because i put the email directly in the footer provision under the main.html template 
    #read about "spread operators" both in javascript and python; e.g the 2 stars used above next to the context in regard to the email address.
    #another way to do it, is just including the email address in the context dictionary

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer', 'admin'])
def userPage(request): 
    
    orders = request.user.customer.order_set.all()
    print('ORDERS:', orders)
    context = {'orders':orders}
    return render(request, 'Jah_Accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):

    products = Product.objects.all()
    return render(request, 'Jah_Accounts/Products.html', {'products': products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request, cust_id):

    customers = Customer.objects.get(id = cust_id)
    orders = customers.order_set.all()  #need to re-go through the exact purpose of this when back online!
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customers': customers, 'orders': orders, 'order_count': order_count, 'customer_name': customers, 'myFilter': myFilter,}
    return render(request, 'Jah_Accounts/Customer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('Product', 'status'), extra=7) #extra 7 helps to add extra 7 forms
    customer = Customer.objects.get(id=pk)
    #form = OrderForm(initial={'Customer': customer,})
    #form above has been commented and replaced by formset (below) such that multiple orders can be made.
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer) #such that we can have multiple forms
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context= {'formset':formset,}
    return render(request, 'Jah_Accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    formset = OrderForm(instance=order)
    if request.method == 'POST':
        formset = OrderForm(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset,}
    return render(request, 'Jah_Accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'Jah_Accounts/delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form,}
    return render(request, 'Jah_Accounts/updateCustomer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createCustomer(request):
    customer = Customer.objects.all()
    form = CustomerForm(initial={'customer': customer})
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context= {'form':form,}
    return render(request, 'Jah_Accounts/createCustomer.html', context)

