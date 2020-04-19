from django.forms import ModelForm
from django.forms import Form
from django import forms
from .models import UserData


class UserDataForm(ModelForm):
    class Meta:
        model = UserData
        fields = ['profilePic', 'bio']


class SignUpForm(Form):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


