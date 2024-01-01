from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Artist,Track

# Artist serializers
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name']

# Track serializers
class TrackSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Track
        fields = ['id','title','genre','artist']

class ArtistAndTracksSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ('id', 'name', 'tracks')

class ArtistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name')

