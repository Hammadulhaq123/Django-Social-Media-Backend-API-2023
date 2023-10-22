from .models import  Events
from rest_framework import serializers
from participants.serializers import ParticipantSerializer


class EventSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)
    class Meta:
        model = Events
        fields = ('id', 'event_name', 'event_description', 'event_date','event_time', 'created_at', 'participants')
