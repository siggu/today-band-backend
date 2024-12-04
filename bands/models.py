from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=255)
    photo = models.URLField()
    formation_date = models.CharField(max_length=10)
    debut_date = models.CharField(max_length=10)
    genre = models.ManyToManyField(Genre)
    members = models.TextField()
    hit_songs = models.CharField(max_length=255)
    albums = models.TextField()
    awards = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "bands"
