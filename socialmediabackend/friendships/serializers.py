from .models import Friends
from rest_framework import serializers

class FriendSerializer(serializers.ModelSerializer):
    followers = serializers.ReadOnlyField(source='friendzoned_by.username')
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Friends
        fields = ['id','user','followers']