
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('blog.urls')),
    url(r'^post$', include('blog.urls')),
    url(r"^search", include('blog.urls')),
    url(r"^thumbnail/(?P<path>.*)$", serve,
        {'document_root': settings.MEDIA_ROOT})
]
