from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Comment
from . import serializers


class Comments(APIView):
    def get(self, request):
        all_comments = Comment.objects.all()
        serializer = serializers.CommentSerializer(
            all_comments,
            many=True,
        )
        return Response(serializer.data)
