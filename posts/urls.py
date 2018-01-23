from django.conf.urls import url, include
from .views import index, create, read, delete, edit

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^create/$', create, name="create"),
    url(r'^read/(?P<id>\d+)/$', read, name='read'),
    #url(r'^delete/(?P<id>\d+)/$', delete, name='delete'),
    url(r'^edit/(?P<id>\d+)/$', edit, name='edit')
]
