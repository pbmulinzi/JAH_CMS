from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'Jah_Accounts/Dashboard.html')

def products(request):
    return render(request, 'Jah_Accounts/Products.html')

def customers(request):
    return render(request, 'Jah_Accounts/Customer.html')