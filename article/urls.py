from django.conf.urls import url,include
from django.contrib import admin
from article.views import *

urlpatterns = [
    url(r'^articles/$', articles, name='articles'),
    url(r'^articles/(?P<id>\d+)/$', article,name='article'),
    url(r'^articles/addcomment/(?P<id>\d+)/$',addcomment,name='addcomment'),
    url(r'^articles/addlike/(?P<id>\d+)$',addlike,name='addlike'),
    url(r'^history/$', history, name='history'),
    url(r'^technique/$',technique, name='technique'),
    url(r'^record/$', record, name='record'),
    url(r'^swimmer/(?P<id>\d+)/$', swimmer, name='swimmer'),
    url(r'^country/(?P<id>\d+)/$', country, name='country'),
    url(r'^home/$', home, name='home'),
    url(r'^page/(\d+)/$',articles),
    url(r'^$', home, name='home'),
]
