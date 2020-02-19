from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class SignUpForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','password','email','first_name','last_name',]


class PersonalDataForm(forms.Form):
   first_name = forms.CharField(required=True, max_length=255)
   last_name = forms.CharField(required=True, max_length=255)
   email = forms.EmailField(required=True)
   phone = forms.CharField(required=True, max_length=200)
   address = forms.CharField(max_length=1000, widget=forms.Textarea())



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','location','birth_date')