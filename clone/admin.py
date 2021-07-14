from django.contrib import admin
from .models import ProfileImages, Photo, Profile, Post, Follow, Tag
# Register your models here.
admin.site.register(Photo)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(ProfileImages)
admin.site.register(Follow)