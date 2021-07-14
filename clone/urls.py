from django.urls import path
from . import views
from django.contrib.auth import logout, views as auth_views

urlpatterns = [
     #authentication urls
    path('accounts/login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('accounts/password_change/',auth_views.PasswordChangeView.as_view(template_name='password_reset_form.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='pasword_change_done.html'),name='password_change_done'),
    path('accounts/password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name='password_reset'),
    path('accounts/password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    #path('accounts/reset/<uidb64>/<token>/' [name='password_reset_confirm']
    #path('accounts/reset/done/' [name='password_reset_complete']



    path('register/',views.register,name="register"),
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('profile', views.profile, name='profile'),
    path('create/', views.ImageCreateView.as_view(), name='create'),
    path('imagelist/',views.ImageListView.as_view(), name='image_list'),
    path('index', views.index, name='index')
   
]
   
