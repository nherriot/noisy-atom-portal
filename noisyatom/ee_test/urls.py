from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from ee_test.views import ee_index_view, ee_calculated_interest

app_name = "ee_test"


app_name = "blogs"

urlpatterns = [
    url('^banking-calculator/$', ee_index_view, name='ee_banking_calculator'),
    url('^calculated/$', ee_calculated_interest, name='ee_calculated_value')
    # url('^dashboard/$', dashboard_view, name='admin_page'),
]
