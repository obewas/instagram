from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from cloudinary.forms import cl_init_js_callbacks
from django.views import generic      
from .models import Photo, Profile, Image, ProfileImages
from .forms import SignUpForm, PhotoForm, UserUpdateForm, ProfileUpdateForm, ImageCreationForm
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

#Image creation, update, deletion, display
def create_image(request):
    if request.method == "POST":
        form = ImageCreationForm(request.POST)
        if form.is_valid():
          image = form.cleaned_data['image']
          image_name = form.cleaned_data['image_name']
          caption = form.cleaned_data['caption']
          profile = form.cleaned_data['profile']
          likes = form.cleaned_data['likes']
          comment = form.cleaned_data['comment']
          form.save()
            # <process form cleaned data>
          return HttpResponseRedirect('/home/')
    else:
        form = ImageCreationForm()

    return render(request, 'image/.html', {'form': form})

class ImageListView(ListView):
  model = ProfileImages
  template_name = 'image/profileimages.html'
  context_object_name = 'profileimages'
  ordering = ['-created_at']




class ImageCreateView(LoginRequiredMixin ,CreateView):
  model = ProfileImages
  fields = ['user','image', 'image_name', 'caption', 'likes','comments']
  template_name = 'image/create_image.html'
  success_url = '/'

  def form_valid(self, form):
      form.instance.created_by = self.request.user
      return super().form_valid(form)
  