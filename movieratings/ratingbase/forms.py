from django import forms
from django.contrib.auth.models import User
from .models import Rater, Movie, Rating


class RaterForm(forms.ModelForm):
    class Meta:
        model = Rater
        fields = ('rater_id', 'gender', 'age', 'occupation', 'zip_code')


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating',)
