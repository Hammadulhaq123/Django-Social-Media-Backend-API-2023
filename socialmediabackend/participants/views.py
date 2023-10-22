from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, viewsets, status
from .permissions import hasSelfParticipatedOrNot
from .serializers import  ParticipantSerializer
from .models import Participant
from events.models import Events

# Create your views here.
class ParticipantViewset(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,hasSelfParticipatedOrNot]

    def perform_create(self, serializer):
        event_instance = get_object_or_404(Events,pk=self.request.data['event'])

        already_participated=Participant.objects.filter(event=event_instance,participated_by=self.request.user).exists()
        if already_participated:
            Participant.objects.filter(event=event_instance,participated_by=self.request.user).delete()
        else:
            serializer.save(participated_by=self.request.user,event=event_instance)