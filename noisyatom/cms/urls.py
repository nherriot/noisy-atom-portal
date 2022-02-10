from django.urls import re_path

app_name = 'cms'


from cms.views import (
        about_us,
        ons_view,
        alfa_view,
        coming_soon,
        index_view,
        vodafone_view,
    )

urlpatterns = [
    re_path('^$', index_view, name='index'),
    re_path('^alfa/$', alfa_view, name='alfa'),
    re_path('^vodafone/$', vodafone_view, name='vodafone'),
    re_path('^coming-soon/$', coming_soon, name='coming_soon'),
    re_path('^about-us/$', about_us, name='about_us'),
    re_path('^ons/$', ons_view, name='ons'),
    #re_path(r'^articles/$', index_view, name='foo_bar_url'),
    # re_path('^dashboard/$', dashboard_view, name='admin_page'),
]
