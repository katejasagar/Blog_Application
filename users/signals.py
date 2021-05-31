from django.db.models.signals import post_save # this is a signal that is fired after the obj is saved
from django.contrib.auth.models import User # user will be our sender, it will be sending the signals
from django.dispatch import receiver # fn who get signal and perform task
from .models import Profile


@receiver(post_save,sender=User ) #decorator saying that evertime user is saved send the signal of post-save
def create_profile(sender,instance,created, **kwargs): # reciever fn to create profile everytime the user is saved
    if created:
        Profile.objects.create(user = instance) # if saved, create the profile for that user instance
 

@receiver(post_save,sender=User ) #decorator saying that evertime user is saved send the signal of post-save
def save_profile(sender,instance, **kwargs): 
        instance.profile.save() # saving the instance
 




