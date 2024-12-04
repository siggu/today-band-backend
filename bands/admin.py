from django.contrib import admin
from .models import Band
from .models import Genre


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "hit_songs",
    )
    search_fields = (
        "name",
        "hit_songs",
    )
    filter_horizontal = ("genre",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
