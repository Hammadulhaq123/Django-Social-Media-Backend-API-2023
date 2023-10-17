from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'auth.User'
        fields = ('id', 'username', 'email', 'password', 'is_active')
        extra_kwargs = {'email': {'required': True,
                                  'write_only': True}, 'password': {'write_only': True}}
