from django.shortcuts import render
from .models import Image


# Create your views here.
def displayphoto(request):
    photos = Image.objects.all()
    return render(request,'photopage.html',{"photos":photos})
