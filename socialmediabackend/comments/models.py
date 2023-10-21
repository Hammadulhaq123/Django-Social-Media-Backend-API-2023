from django.db import models
from posts.models import Posts


# Create your models here.
class Comments(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=1000)
    comment_giphy = models.ImageField(upload_to="comment_gifs", blank=True, null=True)
    comment_date = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return self.comment
