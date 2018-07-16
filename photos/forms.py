from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Photo, Comment


# USERS

# SignUp
class SignUpForm (UserCreationForm):
    email = forms.EmailField ()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# PHOTOS

# Photo
class AddPhotoForm (forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'title', 'description']


# Comment
class AddCommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
