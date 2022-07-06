from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django_countries.fields import CountryField


# # Create your models here.

class Stock(models.Model):
    ticker = models.CharField(max_length=4, blank=False, unique=True)
    name = models.CharField(max_length=200)  
    ## others      

class Portafolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=200)
    country = CountryField(default='Select Country')
    userStock = models.ManyToManyField(Stock)
    def __str__(self):
        return self.user    

