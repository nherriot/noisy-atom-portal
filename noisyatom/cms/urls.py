from django.conf.urls import url

from cms.views import (
        about_us,
        ons_view,
        alfa_view,
        coming_soon,
        index_view,
        vodafone_view,
    )

app_name = "cms"

urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^alfa/$', alfa_view, name='alfa'),
    url(r'^vodafone/$', vodafone_view, name='vodafone'),
    url(r'^coming-soon/$', coming_soon, name='coming_soon'),
    url(r'^about-us/$', about_us, name='about_us'),
    url(r'^ons/$', ons_view, name='ons'),
    #url(r'^articles/$', index_view, name='foo_bar_url'),
    # url(r'^dashboard/$', dashboard_view, name='admin_page'),
]
