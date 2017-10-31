from django.conf.urls import url
from django.contrib import admin

from . import views
from .views import (
		list_post, 
		detail_post,
		create_post,
        update_post,
		delete_post,
	)
   

urlpatterns = [
    url(r'^$', views.list_post, name='list'),
    url(r'^create/$', views.create_post, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail_post, name='detail'),
    url(r'(?P<slug>[\w-]+)/edit/$', views.update_post, name='updated'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.delete_post, name='delete'),
]
