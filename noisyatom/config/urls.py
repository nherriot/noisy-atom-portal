"""
    noisyatom URL Configuration
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'blogs/', include('blogs.urls', namespace='blogs')),
    url(r'ee/', include('ee_test.urls', namespace='ee_test')),
    url(r'', include('cms.urls', namespace='cms')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
