from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.fields import AutoField, PositiveIntegerRelDbTypeMixin
from django.db.models.signals import post_delete, post_save
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
    image = models.ForeignKey(Photo,on_delete=models.CASCADE, null=True)
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
    profile_image = models.ForeignKey(Photo,on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    email = models.EmailField(null=True)
    user_photos = models.ForeignKey(ProfileImages, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.user)

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Tag')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title 

class Post(models.Model):
    picture = models.ImageField(upload_to='media', null=True)
    caption = models.TextField(max_length=1500, verbose_name='Caption')
    posted = models.DateTimeField(auto_now_add=True)
    tags =models.ManyToManyField(Tag, related_name='tags')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField()

    def __str__(self):
        return str(self.posted)

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return str(self.follower)

class Stream(models.Model):
    following = models.ForeignKey(Follow, on_delete=models.CASCADE, related_name='stream_following')
    post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userpost')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def add_post(sender, instance, *args, **kwargs):
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)
        for follower in followers:
            stream = Stream(post=post, user=follower.follower, date=post.posted, following=User.username)
            stream.save()

post_save.connect(Stream.add_post, sender=Post)