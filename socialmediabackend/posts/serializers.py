from rest_framework import serializers
from .models import Posts
from comments.serializers import CommentSerializer
from likes.serializers import LikesSerializer


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer( many=True, read_only=True)
    likes = LikesSerializer(many=True, read_only=True)
    class Meta:
        model = Posts
        fields = ('id', 'content', 'post_image', 'likes','comments', 'category', 'post_date')