from django.conf.urls import url

from cms.views import (
        index_view,
        coming_soon,
        alfa_view,
        about_us,
    )

urlpatterns = [
    url('^$', index_view, name='index'),
    url('^alfa/$', alfa_view, name='alfa'),
    url('^coming-soon/$', coming_soon, name='coming_soon'),
    url('^about-us/$', about_us, name='about_us'),
    #url(r'^articles/$', index_view, name='foo_bar_url'),
    # url('^dashboard/$', dashboard_view, name='admin_page'),
]
