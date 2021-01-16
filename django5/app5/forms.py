from django import forms
from django.contrib.auth.models import User
from app5.models import user_profileinfo

class userform(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model= User
        fields = ( 'username', 'email', 'password')

class user_profileinfoform(forms.ModelForm):
    class Meta():
        model=user_profileinfo
        fields= ( 'portfolio_site', 'profile_pic' )
