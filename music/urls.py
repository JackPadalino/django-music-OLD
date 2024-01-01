from django.urls import path
from . import views,api

app_name="music"

urlpatterns = [
    path("", views.CatalogView.as_view(), name="catalog"),
    path("upload/", views.upload, name="upload"),
    path("download/<int:pk>", views.download, name="download"),
    # api endpoints
    path("api/artists", api.AllArtistsAPIView.as_view(), name="api-all-artists"),
    path("api/artists/<int:pk>", api.SingleArtistAPIView.as_view(), name="api-single-artist"),
    path("api/tracks", api.AllTracksAPIView.as_view(), name="api-all-tracks"),
    path("api/tracks/<int:pk>", api.SingleTrackAPIView.as_view(), name="api-single-track")
]
