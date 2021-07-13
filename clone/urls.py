from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('profile', views.profile, name='profile'),
    path('register/',views.register,name="register"),
    path('create/', views.ImageCreateView.as_view(), name='create'),
    path('imagelist/',views.ImageListView.as_view(), name='image_list'),
    
   
]
   
