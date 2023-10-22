from .models import Participant
from rest_framework import serializers




class ParticipantSerializer(serializers.ModelSerializer):
    participant = serializers.ReadOnlyField(source='participated_by.username')
    event_organizer = serializers.ReadOnlyField(source='event.event_organizer.username')
    event_name = serializers.ReadOnlyField(source='event.event_name')
    class Meta:
        model = Participant
        fields = ['id','event_name','event_organizer','participant']