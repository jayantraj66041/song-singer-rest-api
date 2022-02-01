from rest_framework import serializers
from .models import Singer, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']


class SingerSerializer(serializers.ModelSerializer):
    #  video refrence - https://www.youtube.com/watch?v=dMJUDeKsYtI&list=PLbGui_ZYuhijTKyrlu-0g5GcP9nUp_HlN&index=33

    song = serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field="title")
    
    class Meta:
        model = Singer
        fields = ['id', 'name', 'age', 'gender', 'song']