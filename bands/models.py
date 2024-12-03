from django.db import models


class Bands(models.Model):
    name = models.CharField(max_length=255)
    photo = models.URLField()
    formation_date = models.CharField(max_length=10)
    debut_date = models.CharField(max_length=10)
    genre = models.CharField(max_length=255)
    members = models.TextField()
    hit_songs = models.CharField(max_length=255)
    albums = models.TextField()
    awards = models.TextField()

    def __str__(self):
        return self.name
