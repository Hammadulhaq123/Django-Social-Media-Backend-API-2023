from django.db import models
from posts.models import Posts


# Create your models here.
class Likes(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='likes')
    liked_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self) -> str:
        return self.post.content