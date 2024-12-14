from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from bands.models import Band
from .models import Likes
from .serializers import LikesSerializer, BandSerializer


class LikeBandView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        likes = Likes.objects.filter(user=request.user).first()
        bands = likes.bands.all() if likes else []
        serializer = BandSerializer(bands, many=True)
        return Response(serializer.data)


class LikeBandDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, band_id):
        try:
            band = Band.objects.get(id=band_id)
        except Band.DoesNotExist:
            raise NotFound("Band not found")

        likes, created = Likes.objects.get_or_create(user=request.user)
        if band in likes.bands.all():
            likes.bands.remove(band)
            message = f"{band.name} has been removed from your likes."
        else:
            likes.bands.add(band)
            message = f"{band.name} has been added to your likes."
        return Response({"message": message})
