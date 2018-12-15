from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url(r'^$',views.displayphoto,name='photopage'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile/',views.displayprofile,name='profile'),
    url(r'^comments/',views.displaycomments,name='comments'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)