from django.contrib.auth.models import User
from .models import Movie
from django.contrib.auth.forms import UserCreationForm
from django import forms

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class MovieSearchForm(forms.Form):
    genre = forms.CharField(max_length=100, required=False)
    title = forms.CharField(max_length=100, required=False)
    min_rating = forms.FloatField(min_value=0, max_value=10, required=False)

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movieid', 'title', 'genre', 'director', 'description', 'year', 'image', 'imdblink']