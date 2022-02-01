from msilib.schema import ServiceInstall
from rest_framework.views import APIView
from .serializers import SingerSerializer, SongSerializer
from rest_framework.response import Response
from .models import Song, Singer
from rest_framework import status
# Create your views here.

class SongView(APIView):
    def get(self, request, id=None):
        song = []
        serializer = None
        if id == None:
            song = Song.objects.all()
            serializer = SongSerializer(song, many=True)
        else:
            song = Song.objects.get(id=id)
            serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class SingerView(APIView):
    def get(self, request, id=None):
        singer = []
        serializer = None
        if id == None:
            singer = Singer.objects.all()
            serializer = SingerSerializer(singer, many=True)
        else:
            singer = Singer.objects.get(id=id)
            serializer = SingerSerializer(singer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)