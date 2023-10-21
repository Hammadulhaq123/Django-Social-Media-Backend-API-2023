from django.db import models

# Create your models here.
class Posts(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(max_length=4000)
    post_image = models.ImageField(upload_to='post_image', null=True, blank=True)
    category = models.CharField(max_length=1000,default=None, blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content
