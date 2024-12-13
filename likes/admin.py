from django.contrib import admin
from .models import Likes


@admin.register(Likes)
class LikeAdmin(admin.ModelAdmin):
    pass
