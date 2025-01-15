from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.forms import inlineformset_factory

# Create your views here.

def dashboard(request):

    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    pending = Order.objects.filter(status = 'Pending').count()
    delivered = Order.objects.filter(status = 'Delivered').count()
    Out_for_Delivery =  Order.objects.filter(status = 'Out for delivery').count()

    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'pending': pending, 'delivered': delivered, 'Out_for_Delivery': Out_for_Delivery}
    return render(request, 'Jah_Accounts/Dashboard.html', context)

def products(request):

    products = Product.objects.all()
    return render(request, 'Jah_Accounts/Products.html', {'products': products})

def customers(request, cust_id):

    customers = Customer.objects.get(id = cust_id)
    orders = customers.order_set.all()  #need to re-go through the exact purpose of this when back online!
    order_count = orders.count()

    context = {'customers': customers, 'orders': orders, 'order_count': order_count, 'customer_name': customers,}
    return render(request, 'Jah_Accounts/Customer.html', context)

def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('Product', 'status'))
    customer = Customer.objects.get(id=pk)
    #form = OrderForm(initial={'Customer': customer,})
    #form above has been commented and replaced by formset (below) such that multiple orders can be made.
    formset = OrderFormSet(instance=customer) #such that we can have multiple forms
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context= {'formset':formset,}
    return render(request, 'Jah_Accounts/order_form.html', context)

def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form,}
    return render(request, 'Jah_Accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'Jah_Accounts/delete.html', context)

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
