from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
# Create your views here.


class UserViewset(viewsets.Viewset):

    # List
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    # Create
    def create(self, request):
        pass

    # Retrieve
    def retrieve(self, request):
        pass
