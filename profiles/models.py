from asyncio.windows_events import NULL
from email.policy import default
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Add signal to trigger automatic user creation
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pictures")
    description = models.CharField(max_length=500, blank=True)
    country = CountryField(default='Select Country')
    def __str__(self):
        return f'{self.user.username}\'s Profile...'

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)        