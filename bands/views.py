from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Band
from . import serializers


class Bands(APIView):
    def get(self, request):
        all_bands = Band.objects.all()
        serializer = serializers.BandDetailSerializer(
            all_bands,
            many=True,
        )
        return Response(serializer.data)


class BandDetail(APIView):
    def get_object(self, id):
        try:
            return Band.objects.get(id=id)
        except Band.DoesNotExist:
            raise NotFound

    def get(self, request, id):
        serializer = serializers.BandDetailSerializer(self.get_object(id))
        return Response(serializer.data)

    def delete(self, request, id):
        band = self.get_object(id)
        band.delete()
        return Response(status=HTTP_204_NO_CONTENT)


def make_error(request):
    division_by_zero = 1 / 0
