from django.db import models
from events.models import Events

# Create your models here.

class Participant(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='participants')
    participated_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, default=None, null=True)

    def __str__(self) -> str:
        return(self.event.event_name)
