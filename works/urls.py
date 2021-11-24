from django.urls import path
from web.views import index


app_name = "works"


urlpatterns = [
    path("",index, name="index")

]
