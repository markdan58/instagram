from django.conf.urls import url
from . import views



urlpatterns=[
    url(r'^$',views,name='photopage'),
    url(r'^$',views,name='searchpage'),
]