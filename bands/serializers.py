from rest_framework.serializers import ModelSerializer
from .models import Band


class BandSerializer(ModelSerializer):
    class Meta:
        model = Band
        fields = ("name",)
