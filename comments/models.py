from django.db import models


class Comment(models.Model):
    detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comments",
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "comments"
