from rest_framework import serializers
from .models import Singer, Song


class SongSerializer(serializers.ModelSerializer):
    singer = serializers.StringRelatedField()
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']


class SingerSerializer(serializers.ModelSerializer):
    #  video refrence - https://www.youtube.com/watch?v=dMJUDeKsYtI&list=PLbGui_ZYuhijTKyrlu-0g5GcP9nUp_HlN&index=33

    song = SongSerializer(many=True, read_only=True)    # nested api

    # song = serializers.StringRelatedField(many=True, read_only=True)  # relation of song table
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field="title")

    class Meta:
        model = Singer
        fields = ['id', 'name', 'age', 'gender', 'song']