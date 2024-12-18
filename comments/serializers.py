from rest_framework.serializers import ModelSerializer
from .models import Comment
from rest_framework import serializers


class CommentSerializer(ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "detail", "date", "user"]
        read_only_fields = ["id", "date", "user"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class CommentDetailSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
