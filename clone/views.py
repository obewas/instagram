from django.conf.urls import url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django import forms
from django.http import HttpResponse, request
from django.contrib import messages
from cloudinary.forms import cl_init_js_callbacks
from django.urls.base import reverse_lazy
from django.views import generic      
from .models import Photo, Profile
from .forms import SignUpForm, PhotoForm, NewProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
@login_required(login_url='/accounts/login/')
def new_profile(response):
    current_user = request.user
    if response.method == 'POST':
      form = NewProfileForm(response.POST, request.FILES)
      if form.is_valid():
        profile = form.save(commit=False)
        profile.user = current_user
        profile.save()
      return redirect('home')
    else:
      form = NewProfileForm()
    
    return render(response, 'create_profile.html', {'form':form})

def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()

  return render(request, 'upload.html', context)


def profile(request):
  
  return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            success_url=reverse_lazy('new_profile')

    else:
        f = UserCreationForm()

    return render(request, 'registration/registration_form.html', {'form': f})

def userpage(request):
  user_form = SignUpForm(instance=request.user)
  profile_form = NewProfileForm(instance=request.user.profile)
  return render(request=request, template_name='user.html', context={'user':request.user, 'user_form':user_form, 'profile_form':profile_form})
