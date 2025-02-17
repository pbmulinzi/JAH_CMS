
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                user_groups = request.user.groups.values_list('name', flat = True)
                if any(group in allowed_roles for group in user_groups):
                    return view_func(request, *args, **kwargs)                
            return HttpResponse('You are not allowed to view this page.')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.groups.exists():
            group = request.user.groups.first().name
            if group == 'customer':
                return redirect ('user-page')
            elif group == 'admin':
                return view_func(request, *args, **kwargs)
        return redirect('register')
    return wrapper_function


                









'''
from django.http import HttpResponse
from django.shortcuts import redirect

from django.core.exceptions import ObjectDoesNotExist


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            try:
                customer = request.user.customer
                group = customer.user.groups.first().name if customer.user.groups.exists() else None
            except ObjectDoesNotExist:
                # Handle the case where the customer does not exist
                return HttpResponse('You do not have a customer profile.')

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to view this page.')
        return wrapper_func
    return decorator
'''



'''   

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            #group = None
            if request.user.groups.exists():
                #group = request.user.groups.all()[0].name
                #Changing coz the line above only caters for only one group(the first group), while the line below caters for users belonging to multiple groups
                groupss = request.user.groups.values_list('name', flat=True)
            else:
                group = [] #default to an empty list if no group exists

            if any(group in allowed_roles for group in groupss):
                return view_func(request, *args, **kwargs)

            #if group in allowed_roles:
            #  return view_func(request, *args, **kwargs)

            else:
                return HttpResponse('You are not allowed to view this page.')
        return wrapper_func
    return decorator
'''



'''
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        #group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        else:
            group = []  # Default to empty list if no groups exi

        print(f"User group: {group}") #debugging

        if group == 'customer':
            print('Redirecting to user-page...') #debugging
            return redirect('user-page')
        
        if group == 'admin':
            print('Proceeding to dashboard...') #debugging
            return view_func(request, *args, **kwargs)
        
        print('Redirecting to home...') #debugging
        return redirect('home') #redirect users with no group to home
        #return redirect('/')
        
    return wrapper_function

'''