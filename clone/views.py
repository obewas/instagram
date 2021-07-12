from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django import forms
from django.http import HttpResponse
from django.contrib import messages
from cloudinary.forms import cl_init_js_callbacks
from django.urls.base import reverse_lazy
from django.views import generic      
from .models import Photo, Profile
from .forms import SignUpForm, PhotoForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.


def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()
        return redirect('profile')
  return render(request, 'upload.html', context)

@login_required
def home(request):

  profile = Profile.objects.all()
  context = {
    'profile':profile

  }
  return render(request, 'home.html', context)


def register(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Your account has been created!')
      return redirect('profile')
  else:
    form = SignUpForm()
  return render(request, 'registration/registration_form.html', {'form':form})

@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
      'u_form':u_form, 'p_form':p_form
    }

    return render(request, 'profile.html', context)