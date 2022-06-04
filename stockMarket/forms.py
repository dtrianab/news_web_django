from django.forms import ModelForm
from .models import Portafolio
from django.contrib.postgres.forms import SimpleArrayField
from django import forms
from django_countries.fields import CountryField

#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
#from .models import Profile

class RegisterTicker(forms.Form):
    #name = forms.CharField(max_length=200)
    #tags = SimpleArrayField(forms.CharField(max_length=4, required=False))
    tag = forms.CharField(max_length=4, help_text="Company Ticker")
    # class Meta:
    #     model = Portafolio
    #     fields = ['ticker']


class RegisterPortafolio(forms.Form):
    name = forms.CharField(max_length=200)
    country = CountryField().formfield()
    class Meta:
        model = Portafolio
        fields = ['name', 'country']
