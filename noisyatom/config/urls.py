"""
    noisyatom URL Configuration
"""

from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'blogs/', include('blogs.urls', namespace='blogs')),
    re_path(r'ee/', include('ee_test.urls', namespace='ee_test')),
    re_path(r'', include('cms.urls', namespace='cms')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
