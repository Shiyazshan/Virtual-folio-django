from django.urls import path
from works import views


app_name = "works"


urlpatterns = [
    path('/', views.index),
]
