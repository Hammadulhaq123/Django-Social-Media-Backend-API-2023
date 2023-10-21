from .models import Likes
from rest_framework import serializers

class LikesSerializer(serializers.ModelSerializer):
    liked_by = serializers.ReadOnlyField(source='liked_by.username')
    post_owner = serializers.ReadOnlyField(source='post.owner.username')
    class Meta:
        model = Likes
        fields = ['id','post_owner','liked_by']