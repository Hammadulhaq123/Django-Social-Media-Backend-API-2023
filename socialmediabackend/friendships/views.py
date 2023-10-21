from .permissions import hasSelfFollowedOrReadOnly
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, viewsets,status,permissions
from . models import Friends
from . serializers import FriendSerializer
from django.contrib.auth.models import User


# Create your views here.
class FriendsViewset(viewsets.ModelViewSet):

    queryset=Friends.objects.all()
    serializer_class=FriendSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,hasSelfFollowedOrReadOnly]

    def perform_create(self, serializer):
        user_instance=get_object_or_404(User,pk=self.request.data['user'])

        already_followed=Friends.objects.filter(user=user_instance,friendzoned_by=self.request.user).exists()
        if already_followed:
            Friends.objects.filter(user=user_instance,friendzoned_by=self.request.user).delete()
        else:
            serializer.save(friendzoned_by=self.request.user,user=user_instance)
       
        