from django.contrib import admin
from .models import Bands


@admin.register(Bands)
class BandAdmin(admin.ModelAdmin):
    pass
