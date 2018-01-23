from django.conf.urls import url

from cms.views import (
        about_us,
        ons_view,
        alfa_view,
        coming_soon,
        index_view,
        vodafone_view,
    )

urlpatterns = [
    url('^$', index_view, name='index'),
    url('^alfa/$', alfa_view, name='alfa'),
    url('^vodafone/$', vodafone_view, name='vodafone'),
    url('^coming-soon/$', coming_soon, name='coming_soon'),
    url('^about-us/$', about_us, name='about_us'),
    url('^ons/$', ons_view, name='ons'),
    #url(r'^articles/$', index_view, name='foo_bar_url'),
    # url('^dashboard/$', dashboard_view, name='admin_page'),
]
