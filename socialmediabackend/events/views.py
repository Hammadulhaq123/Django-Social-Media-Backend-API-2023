from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, viewsets, status
from user_profile.permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer
from .models import Events

# Create your views here.

# Viewset for all events:
class EventsViewset(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # user can only create a post under his owenrship and can only update or delete his posts not anyone else's
    def perform_create(self, serializer):
        serializer.save(event_organizer=self.request.user)


