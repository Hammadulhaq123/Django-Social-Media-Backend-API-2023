from .models import Likes
from rest_framework import serializers

class LikesSerializer(serializers.ModelSerializer):
    liked_by = serializers.ReadOnlyField(source='liked_by.username')
    class Meta:
        model = Likes
        fields = ['id','post','liked_by']