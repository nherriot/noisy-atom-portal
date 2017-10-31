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
    url(r'blog/', include('blogs.urls', namespace='blogs')),
    url(r'comments/', include('comments.urls', namespace='comments')),
    url(r'', include('cms.urls', namespace='cms')),
    url(r'', include('ee_test.urls', namespace='ee_test')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
