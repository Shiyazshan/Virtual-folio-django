from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("web.urls",namespace="web")),
    path("",include("users.urls",namespace="users"))
]
