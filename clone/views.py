from django.conf import settings
from django.core.mail import send_mail
from django_project import helpers
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
from .forms import PhotoForm, CreateNewProfile, CustomUserCreationForm
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

def register(request):
    if request.method == 'POST':
      f = CustomUserCreationForm(request.POST)
      if f.is_valid():
          # send email verification now
          activation_key = helpers.generate_activation_key(username=request.POST['username'])

          subject = "TheGreatDjangoBlog Account Verification"

          message = '''\n
        Please visit the following link to verify your account \n\n{0}://{1}/cadmin/activate/account/?key={2}
                                '''.format(request.scheme, request.get_host(), activation_key)

          error = False

          try:
              send_mail(subject, message, settings.SERVER_EMAIL, [request.POST['email']])
              messages.add_message(request, messages.INFO,
                                   'Account created! Click on the link sent to your email to activate the account')

          except:
              error = True
              messages.add_message(request, messages.INFO, 'Unable to send email verification. Please try again')
          if not error:
              u = User.objects.create_user(
                  request.POST['username'],
                  request.POST['email'],
                  request.POST['password1'],
                  is_active=0
              )
              profile = Profile()
              profile.activation_key = activation_key
              profile.user = u
              profile.save()

          return redirect('register')

      else:
       f = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': f})