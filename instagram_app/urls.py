from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url(r'^$',views.displayphoto,name='photopage'),
     url(r'^search/', views.search_profile, name='search_profile'),
    url(r'^accounts/profile/',views.displayprofile,name='profile'),
    url(r'^comment/(\d+)/',views.displaycomments,name='comment'),
    url(r'^register',views.register, name='register'),
    url(r'^likes',views.like, name='like'),
    url(r'^searched_profile/(\d+)/',views.searched_profile, name='searched_profile'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)