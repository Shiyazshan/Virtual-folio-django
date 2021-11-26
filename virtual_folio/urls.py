from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("web.urls",namespace="web")),
    path("",include("users.urls",namespace="users")),
    path("works/",include("works.urls",namespace="works")),
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
