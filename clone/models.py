from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Photo(models.Model):
    name= models.CharField(max_length=100)
    image = CloudinaryField('image')


class Profile(models.Model):
    name = models.CharField(max_length=200)
    image = models.ForeignKey(Photo, on_delete=models.CASCADE)
    bio = models.TextField()