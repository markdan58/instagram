from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from .models import Image,Profile,Comments
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,CommentsForm
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse,Http404
from .email import activation_email


# Create your views here.

def displayphoto(request):
    photos = Image.objects.all()
    comment = Comments.objects.all()
    return render(request,'photopage.html',{"photos":photos})



@login_required(login_url='/accounts/login/')
def displayprofile(request):
    profiles = Profile.objects.all()
    return render(request,'profile.html',{"profiles":profiles})


@login_required(login_url='/accounts/login')
def displaycomments(request,image_id):
    images = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.profile = request.user.profile
            comment.photo = images
            comment.save()
        return redirect('photopage')

    else:

        return redirect(request,'photopage.html')


@login_required(login_url='/accounts/login/')
def search_profile(request):
    if 'profile' in request.GET and request.GET['profile']:
        search_term = request.GET.get('profile')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Type profile'
        return render(request, 'search.html', {'message':message})


def register(request):
    if request.user.is_authenticated():
        return redirect('photopage')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                to_email = form.cleaned_data.get('email')
                activation_email(user, current_site, to_email)
                return HttpResponse('Please confirm your email')
        else:
            form = RegistrationForm()
        return render(request, 'registration/registration_form.html',{'form':form})

 
def like(request):
    photolikes = likingphoto(request.Get, request.Image)
    context = {'pic_output':ajax.output()}
    return render(request,'photopage',context)
    