from django import forms
from .models import Image,Profile,Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [ 'comment' ]


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text = 'Required')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')




class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes','profile','comment']