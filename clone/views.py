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
from .models import Photo, Profile, Image, ProfileImages, Stream, Post
from .forms import SignUpForm, PhotoForm, UserUpdateForm, ProfileUpdateForm, ImageCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .email import send_welcome_email
from django.template import loader
# Create your views here.

# uploading photo to the app
def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':

    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()
        return redirect('profile')
  return render(request, 'upload.html', context)

#for displaying profile page to the authenticated user
@login_required
def home(request):

  profile = Profile.objects.all()
  context = {
    'profile':profile

  }
  return render(request, 'home.html', context)

# for registering a new user
def register(request):
  name = Profile.name
  email = Profile.email
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
  
      messages.success(request, f'Your account has been created!')
      recipient = Profile(name=name, email=email)
      recipient.save()
      send_welcome_email(name,email)
      return redirect('profile')
  else:
    form = SignUpForm()
  return render(request, 'registration/registration_form.html', {'form':form})
# for creating a new user profile
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

@login_required
def index(request):
  user = request.user
  posts = Stream.objects.filter(user=user)
  group_ids = []
  for post in posts:
    group_ids.append(post.post_id)
  post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
  template = loader.get_template('index.html')
  context = {
    'post_items':post_items
  }

  return HttpResponse(template.render(context, request))
  