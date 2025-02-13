from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Customer

#for debugging purposes of some errors
from django.dispatch import receiver


@receiver(post_save, sender=User) #creating related objects automatically
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group, group_created = Group.objects.get_or_create(name='customer')
        print(group)
        instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            name=instance.username,
        )
        print('Customer Profile Created!')

@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    '''Saves the related customer instance when the user instance is saved'''
    instance.customer.save()

    '''
    customer = getattr(instance, 'customer', None) #prevents attribute error
    if customer:
        customer.save()
    '''

        



#post_save.connect(customer_profile, sender=Customer)

#commented the code below because of some possible causes of infinite loops. Replaced it with the code written above.
'''
def customer_profile(sender, instance, created, **kwargs):

    if created:
        group = Group.objects.get_or_create(name = 'customer')

        print(group)
        if (group != None):

            instance.groups.add(group)

            Customer.objects.create(
                user = instance,
                name = instance.username,
            ) 
            print('Profile Created!') 
post_save.connect(customer_profile, sender=Customer)

'''



@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Profile updated!')
post_save.connect(update_profile, sender=User)

