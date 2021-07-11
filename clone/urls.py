from os import name
from django.urls import path
from .views import upload, profile, userpage,register, new_profile

urlpatterns = [
  
    path('upload/', upload, name='upload'),
    path('profile', profile, name='profile'),
    path('register/', register, name='register'),
    path("user", userpage, name = "userpage"),
    path('new_profile/', new_profile, name='new_profile'),
]