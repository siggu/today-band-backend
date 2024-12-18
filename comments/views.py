from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Comment
from . import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Comments(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_comments = Comment.objects.all()
        serializer = serializers.CommentSerializer(
            all_comments,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CommentSerializer(
            data=request.data,
            context={"request": request},
        )
        if serializer.is_valid():
            comment = serializer.save()
            return Response(serializers.CommentSerializer(comment).data)
        return Response(serializer.errors, status=400)


class CommentDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, id):
        try:
            return Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            raise NotFound

    def get(self, request, id):
        comment = self.get_object(id)
        serializer = serializers.CommentDetailSerializer(comment)
        return Response(serializer.data)

    def delete(self, request, id):
        comment = self.get_object(id)
        if not request.user.is_authenticated:
            raise PermissionDenied("로그인 후 이용 가능합니다.")
        if comment.user != request.user:
            raise PermissionDenied("본인이 작성한 댓글만 삭제할 수 있습니다.")
        comment.delete()
        return Response(status=HTTP_204_NO_CONTENT)
