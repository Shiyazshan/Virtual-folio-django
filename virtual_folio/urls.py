from django.contrib import admin
from django.urls import path,include
from works import urls as works_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("web.urls",namespace="web")),
    # path("",include("users.urls",namespace="users")),
    # path("",include("works.urls",namespace="works")),
    path('works/',include(works_urls))
]
