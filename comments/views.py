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

    def post(self, request):
        serializer = serializers.CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()
            serializer = serializers.CommentSerializer(comment)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class CommentDetail(APIView):
    def get_object(self, id):
        try:
            return Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            raise NotFound

    def get(self, request, id):
        serializer = serializers.CommentDetailSerializer(self.get_object(id))
        return Response(serializer.data)
