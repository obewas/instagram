from django.contrib.auth import login
from django.db.models import fields
from django.forms import ModelForm      
from .models import Photo, Profile

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
class PhotoForm(ModelForm):
  class Meta:
      model = Photo
      fields = ['name', 'image']

class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)

	class Meta:
		model = User
		fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2' ]

class CreateNewProfile(forms.ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'