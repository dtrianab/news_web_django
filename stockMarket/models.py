from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# # Create your models here.
class Portafolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    tags = ArrayField(models.CharField(max_length=4), blank=True)
    def __str__(self):
        return self.user    