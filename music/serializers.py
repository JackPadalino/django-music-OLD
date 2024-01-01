from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Artist,Track

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name']

class TrackSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Track
        fields = ['id','title','genre','artist']