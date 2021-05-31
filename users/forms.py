from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):#creating the model form that allow us to work with specific db model
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email'] #our profile will be in the profile model. This is user model

class ProfileUpdateForm(forms.ModelForm): #seperate form for profile
    class Meta:
        model = Profile
        fields = ['image']