from django.db.models.signals import post_save
from .models import Profile
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings

@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
