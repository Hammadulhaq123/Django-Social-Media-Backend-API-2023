from django.db import models

# Create your models here.
class Events(models.Model):
    event_organizer = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="events")
    event_name = models.CharField(max_length=200)
    event_description = models.TextField(max_length=2000)
    created_at = models.DateField(auto_now_add=True)
    event_time = models.TimeField()
    event_date = models.DateField()
    event_location = models.CharField(max_length=1000, default="Virtual Event")
    event_thumbnail = models.ImageField(upload_to="event_images", blank=True)

    def __str__(self) -> str:
        return self.event_name

