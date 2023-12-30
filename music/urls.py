from django.urls import path
from . import views

app_name="music"

urlpatterns = [
    path("", views.catalog, name="catalog"),
    path("upload/", views.upload, name="upload")
]
