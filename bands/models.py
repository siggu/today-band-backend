from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ClassificationChoices(models.TextChoices):
    GA = ("ga", "가")
    NA = ("na", "나")
    DA = ("da", "다")
    RA = ("ra", "라")
    MA = ("ma", "마")
    BA = ("ba", "바")
    SA = ("sa", "사")
    AH = ("ah", "아")
    JA = ("ja", "자")
    CHA = ("cha", "차")
    KA = ("ka", "카")
    TA = ("ta", "타")
    PA = ("pa", "파")
    HA = ("ha", "하")


class Band(models.Model):
    name = models.CharField(max_length=255)
    photo = models.TextField(null=True)
    formation_date = models.CharField(max_length=10)
    debut_date = models.CharField(max_length=10)
    genre = models.ManyToManyField(Genre)
    members = models.TextField()
    hit_songs = models.CharField(max_length=255)
    introduction = models.TextField(null=True)
    music_photo = models.TextField(null=True)
    albums = models.TextField()
    awards = models.TextField()
    classification = models.CharField(
        max_length=3, choices=ClassificationChoices.choices, default="ga"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "bands"
