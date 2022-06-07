
from django import forms
from .models import *
from django.forms import ModelForm




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname','profile_img','bio','email_phone']