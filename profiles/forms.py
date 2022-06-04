from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    country = CountryField().formfield()
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'country']
       # widgets = {'country': CountrySelectWidget()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)      
    class Meta:
        model = User
        fields = [ 'email', 'username', 'first_name', 'last_name']
        #widgets = {'country': CountrySelectWidget()}

class ProfileUpdateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    country = CountryField().formfield()     
    class Meta:
        model = Profile
        fields = ['description', 'image', 'country']        