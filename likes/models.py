from django.db import models
from common.modles import CommonModel


class Likes(CommonModel):
    bands = models.ManyToManyField("bands.Band")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
