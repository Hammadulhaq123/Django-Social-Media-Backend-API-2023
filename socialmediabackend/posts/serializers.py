from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'content', 'post_image', 'category', 'post_date')