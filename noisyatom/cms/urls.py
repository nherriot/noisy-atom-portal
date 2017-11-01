from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from cms.views import index_view, coming_soon, about_us


urlpatterns = [
    url('^$', index_view, name='index'),
    url('^coming-soon/$', coming_soon, name='coming_soon'),
    url('^about-us/$', about_us, name='about_us')
    #url(r'^articles/$', index_view, name='foo_bar_url'),
    # url('^dashboard/$', dashboard_view, name='admin_page'),
]
