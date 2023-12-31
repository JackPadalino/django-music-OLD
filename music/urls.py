from django.urls import path
from . import views

app_name="music"

urlpatterns = [
    path("", views.CatalogView.as_view(), name="catalog"),
    path("upload/", views.upload, name="upload"),
    # path("upload-track/", views.upload_track, name="upload_track")
]
