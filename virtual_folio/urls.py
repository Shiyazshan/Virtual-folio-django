from django.contrib import admin
from django.urls import path,include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from web import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("web.urls",namespace="web")),
    path("works/",include("works.urls",namespace="works")),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)