from django.shortcuts import render,redirect
from .models import Image,Profile,Comments
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def displayphoto(request):
    photos = Image.objects.all()
    commentview = Comments.objects.all()
    print(commentview)
    return render(request,'photopage.html',{"photos":photos})



@login_required(login_url='/accounts/login/')
def displayprofile(request):
    profiles = Profile.objects.all()
    return render(request,'profile.html',{"profiles":profiles})



@login_required(login_url='/accounts/login/')
def displaycomments(request):
    if 'Newcomments' in request.GET and request.GET["Newcomments"]:
        comments = request.GET.get("Newcomments")

        Comments.objects.create(comment = comments) 

    return redirect('photopage')


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'Image' in request.GET and request.GET["Image"]:
        image = request.GET.get("Image")
        looked_Image = Image.search_category(image)
        message = f"{image}"

        return render(request, 'search.html',{"message":message,"images": looked_Image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})