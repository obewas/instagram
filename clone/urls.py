from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('profile/', views.profile, name='profile'),
    path('activate/account/', views.activate_account, name='activate'),
    path('register/', views.register, name='register'),
    
]