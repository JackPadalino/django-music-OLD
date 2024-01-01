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

class AllTracksAPIView(APIView):
    def get(self,request,format=None):
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class ProjectTopicAPIView(APIView):
#     def get(self,request,format=None):
#         topics = ProjectTopic.objects.all()
#         serializer = ProjectTopicSerializer(topics,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class AllProjectsAPIView(APIView):
#     def get(self,request,format=None):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class SingleProjectAPIView(APIView):
#     def get(self,request,pk,format=None):
#         project = Project.objects.get(pk=pk)
#         serializer = ProjectSerializer(project)
#         return Response(serializer.data, status=status.HTTP_200_OK)
