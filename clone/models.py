from django.db import models
import cloudinary
# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=50)
    image = cloudinary.models.CloudinaryField('image')


class Profile(models.Model):
    name = models.CharField(max_length=200)
    image = models.ForeignKey(Photo, on_delete=models.CASCADE)
    bio = models.TextField()