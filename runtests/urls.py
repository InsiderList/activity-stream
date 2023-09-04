import os
from django.contrib import admin
from django.views.static import serve
from django.urls import include, path, re_path


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve,
        {'document_root': os.path.join(os.path.dirname(__file__), 'media')}),
    path('auth/', include('django.contrib.auth.urls')),
    path('testapp/', include('testapp.urls')),
    path('', include('actstream.urls')),
]
