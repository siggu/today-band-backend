from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Band
from . import serializers


class Bands(APIView):
    def get(self, request):
        all_bands = Band.objects.all()
        serializer = serializers.BandSerializer(
            all_bands,
            many=True,
        )
        return Response(serializer.data)
