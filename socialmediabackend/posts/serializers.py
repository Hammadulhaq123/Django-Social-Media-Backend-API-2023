from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'content', 'post_image', 'category', 'post_date')