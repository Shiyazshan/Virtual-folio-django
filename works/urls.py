from django.urls import path
from works.views import index


app_name = "works"


urlpatterns = [
    path("works/index",index, name="index")

]
