from rest_framework import serializers
from django.contrib.auth.models import User
from user_profile.serializers import ProfileSerializer

class UserSerializer(serializers.ModelSerializer):
    profile_data = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name','last_name','email', 'password', 'profile_data','is_active')
        extra_kwargs = {'email': {'required': True,
                                  'write_only': True}, 'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
