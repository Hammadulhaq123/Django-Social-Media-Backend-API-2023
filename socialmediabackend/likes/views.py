from posts.models import Post
from likes.permissions import hasSelfLikedOrReadOnly
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, viewsets,status,permissions
from . models import Likes
from . serializers import LikesSerailizer


# Create your views here.
class LikesViewset(viewsets.ModelViewSet):

    queryset=Likes.objects.all()
    serializer_class=LikesSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,hasSelfLikedOrReadOnly]

    def perform_create(self, serializer):
        post_instance=get_object_or_404(Post,pk=self.request.data['post'])

        already_liked=Likes.objects.filter(post=post_instance,liked_by=self.request.user).exists()
        if already_liked:
            Likes.objects.filter(post=post_instance,liked_by=self.request.user).delete()
        else:
            serializer.save(liked_by=self.request.user,post=post_instance)
       
        