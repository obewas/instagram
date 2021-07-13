from PIL import Image
from django.contrib.auth import login
from django.db.models import fields
from django.forms import ModelForm      
from .models import Photo, Profile, ProfileImages

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

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2' ]

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['profile_image','profession', 'phone', 'mobile', 'address']

class ImageCreationForm:
	class Meta:
		model = ProfileImages
		fields = ['image', 'image_name']

