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
from .forms import SignUpForm, PhotoForm, CreateNewProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
@login_required
def profile(response):
    if response.method == 'POST':
      form = CreateNewProfile(response.POST)

      if form.is_valid():
        n = form.cleaned_data['name']
        t = Profile(name=n)
        t.save()
        response.user.profile.add(t)
        return HttpResponseRedirect("/%" %t.id)
    else:
      form = CreateNewProfile()
    return render(response, 'profile.html', {'form':form})

def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()

  return render(request, 'upload.html', context)


def home(request):
  profile = Profile.objects.all()
  context = {
    'profile':profile

  }
  return render(request, 'home.html', context)


class UserRegisterView(generic.CreateView):
  form_class = SignUpForm
  template_name = 'registration/registration_form.html'
  success_url = reverse_lazy('login')