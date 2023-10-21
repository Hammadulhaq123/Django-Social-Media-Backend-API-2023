from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from user_profile.permissions import IsOwnerOrReadOnly
from .models import Posts

# Create your views here.


class PostsViewset(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)