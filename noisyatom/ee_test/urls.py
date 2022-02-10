from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static

app_name = 'ee_test'

from ee_test.views import ee_index_view, ee_calculated_interest


urlpatterns = [
    re_path('^banking-calculator/$', ee_index_view, name='ee_banking_calculator'),
    re_path('^calculated/$', ee_calculated_interest,  name='ee_calculated_value')
    # re_path('^dashboard/$', dashboard_view, name='admin_page'),
]
