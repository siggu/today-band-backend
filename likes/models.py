from django.db import models


class Likes(models.Model):
    bands = models.ManyToManyField("bands.Band")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "likes"
