from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
# Create your views here.


class UserViewset(viewsets.ViewSet):

    # List
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    # Create
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve
    def retrieve(self, request, pk):
        queryset = User.objects.all()
        lookup_field = 'username'
        user = get_object_or_404(queryset, username=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
