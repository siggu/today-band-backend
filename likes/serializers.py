from rest_framework import serializers
from bands.models import Band
from .models import Likes


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = (
            "id",
            "name",
        )


class LikesSerializer(serializers.ModelSerializer):
    bands = BandSerializer(many=True, read_only=True)

    class Meta:
        model = Likes
        fields = ["user", "bands"]
