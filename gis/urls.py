from django.urls import path
from . import views


app_name = "gis"

urlpatterns = [
      path("", views.index, name="index"),
]