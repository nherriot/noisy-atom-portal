from django.conf.urls import url
from django.contrib import admin

from .views import (
		list_post, 
		detail_post,
		create_post,
        update_post,
		delete_post,
	)
   

urlpatterns = [
    url(r'^$', list_post, name='list'),
    url(r'^create/$', create_post, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', detail_post, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', update_post, name='updated'),
    url(r'^(?P<slug>[\w-]+)/delete/$', delete_post, name='delete'),
]
