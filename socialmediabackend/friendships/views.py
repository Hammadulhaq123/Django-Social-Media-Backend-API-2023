from .permissions import hasSelfFollowedOrReadOnly
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, viewsets,status,permissions
from . models import Friends
from . serializers import FriendSerializer
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
class FriendsViewset(viewsets.ModelViewSet):

    queryset=Friends.objects.all()
    serializer_class=FriendSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,hasSelfFollowedOrReadOnly]

    def perform_create(self, serializer):
        user_instance=get_object_or_404(User,pk=self.request.data['user'])

        if(self.request.user == user_instance):
            messages.error(self.request,"You can't' follow yourself")
        else:
            already_followed=Friends.objects.filter(user=user_instance,friendzoned_by=self.request.user).exists()
            if already_followed:
                Friends.objects.filter(user=user_instance,friendzoned_by=self.request.user).delete()
                messages.info(self.request,"Unfollowed succesfully")

            else:
                serializer.save(friendzoned_by=self.request.user,user=user_instance)
                messages.info(self.request,"Followed succesfully")

       
        