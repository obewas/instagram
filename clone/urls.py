from django.urls import path
from .views import home, upload, profile, register

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload, name='upload'),
    path('profile', profile, name='profile'),
    path('register/',register,name="register"),
]