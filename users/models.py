from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #creatin profile field with one to one relation to users 
    image = models.ImageField(default ='default.jpg', upload_to = 'profile_pics') #adding extra field of image and uploading to dir specified
    
    def __str__(self): #dunder str method to display what to display
        return f'{self.user.username} Profle '
    # since we chaned db model here we need to make migrations in the db via cmd
    # also we need to install pillow to save images
    # also we register models in admin .py