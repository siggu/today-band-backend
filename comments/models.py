from django.db import models


class Comment(models.Model):
    detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "comments"
