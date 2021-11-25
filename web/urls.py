from django.urls import path
from web.views import index


app_name = "web"


urlpatterns = [
    path("web/index",index, name="index")
]
