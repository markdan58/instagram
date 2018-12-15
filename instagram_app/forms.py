from django import forms
from .models import Image


class commentsform(forms.Form):
    comments = forms.CharField(max_length=30)
