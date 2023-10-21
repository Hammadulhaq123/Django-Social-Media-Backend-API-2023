from rest_framework import serializers
from .models import Comments

class CommentSerializer(serializers.ModelSerializer):
    commented_by = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comments
        fields = ('id', 'commented_by', 'post', 'comment', 'comment_giphy', 'comment_date')