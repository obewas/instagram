from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.fields import AutoField
from django.db.models.signals import post_save
# Create your models here.
class Photo(models.Model):
    name= models.CharField(max_length=100)
    image = CloudinaryField('image')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    #def save(self):
     #   super().save()

      #  img = Image.open(self.image.path)
      #  if img.height > 300 or img.width > 300:
      #      output_size  = (300,300)
      #      img.thumbnail(output_size)
       #     img.save(self.image.path)
class ProfileImages(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True)
    image_name = models.CharField(max_length=100)
    caption = models.TextField()
    likes = models.BooleanField(default=True)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.image_name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    email = models.EmailField(null=True)
    user_photos = models.ForeignKey(ProfileImages, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.user)


