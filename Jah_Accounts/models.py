from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    profile_picture = models.ImageField(null=True, default='avi.jpg', blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name or 'Unnamed Customer'
    
class Product(models.Model):
    CATEGORY = (
        ('Flour', 'Flour'),
        ('Honey', 'Honey'),
        ('Spice', 'Spice'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'), 
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    MEASUREMENT = (
        ('Kgs', 'Kgs'),
        ('Tins', 'Tins'),
    )
    Customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL,)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    tags = models.ManyToManyField(Tag)
    Quantity = models.CharField(null=True, max_length=4)
    units = models.CharField(max_length=200, null=True, choices=MEASUREMENT,)
    note = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.Product.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True) 
    last_name = models.CharField(max_length=200, null=True, blank=True) 
    phone = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)

      