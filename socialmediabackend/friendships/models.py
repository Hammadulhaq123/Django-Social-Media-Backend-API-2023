from django.db import models
from posts.models import Posts

# Create your models here.
class Friends(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='followers', null=True, blank=True)
    friendzoned_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None, blank=True, null=True)

