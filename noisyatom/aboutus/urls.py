from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'aboutus'

urlpatterns = [
    # path('', views.index, name='index'),
    path('team/', views.team, name='team'),
    path('', views.aboutus, name='aboutus'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
