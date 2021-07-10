from django.urls import path
from .views import home, upload, UserRegisterView, profile

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload, name='upload'),
    path('profile', profile, name='profile'),
    path('register/', UserRegisterView.as_view(), name="register"),
]