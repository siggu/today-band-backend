from django.db import models


class Comments(models.Model):
    detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True)