from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Photo(models.Model):
    name= models.CharField(max_length=100)
    image = CloudinaryField('image')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ForeignKey(Photo, on_delete=models.CASCADE)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Image(models.Model):
    name = models.CharField(max_length=100, default='image')
    caption = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.BooleanField(default=True)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    