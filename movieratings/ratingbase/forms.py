from django import forms
from django.contrib.auth.models import User
from .models import Rater, Movie, Rating


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class RaterForm(forms.ModelForm):
    class Meta:
        model = Rater
        fields = ('rater_id', 'gender', 'age', 'occupation', 'zip_code')
