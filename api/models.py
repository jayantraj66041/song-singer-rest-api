from operator import mod
from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=30)
    duration = models.IntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title