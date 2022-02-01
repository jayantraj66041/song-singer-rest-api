from rest_framework import serializers
from .models import Singer, Song

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'name', 'age', 'gender']

class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']