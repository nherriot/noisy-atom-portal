from django.urls import re_path
from django.contrib import admin

app_name = 'blogs'

from .views import (
		list_post, 
		detail_post,
		create_post,
        update_post,
		delete_post,
	)
   

urlpatterns = [
    re_path(r'^$', list_post, name='list'),
    re_path(r'^create/$', create_post, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', detail_post, name='detail'),
    re_path(r'(?P<slug>[\w-]+)/edit/$', update_post, name='updated'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', delete_post, name='delete'),
]
