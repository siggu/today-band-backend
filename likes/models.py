from django.db import models


class Likes(models.Model):
    bands = models.ManyToManyField("bands.Band", related_name="liked_by")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "likes"
