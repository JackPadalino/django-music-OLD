# imports for Django Rest Framework
from rest_framework import permissions, viewsets

# imports needed to create our own views
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# imports needed to use DRJ 'APIView'
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ArtistSerializer,TrackSerializer,ArtistAndTracksSerializer
from .models import Artist,Track

class AllArtistsAPIView(APIView):
    def get(self,request,format=None):
        artists = Artist.objects.all()
        serializer = ArtistAndTracksSerializer(artists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleArtistAPIView(APIView):
    def get(self,request,pk,format=None):
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistAndTracksSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AllTracksAPIView(APIView):
    def get(self,request,format=None):
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleTrackAPIView(APIView):
    def get(self,request,pk,format=None):
        track = Track.objects.get(pk=pk)
        serializer = TrackSerializer(track)
        return Response(serializer.data, status=status.HTTP_200_OK)
