from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    last_viewed_at = models.DateTimeField(null=True, blank=True)
    last_viewer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='last_viewed_posts', on_delete=models.SET_NULL, null=True, blank=True)
    
    def update_last_viewed(self, user):
        self.last_viewed_at = timezone.now()
        self.last_viewer = user
        self.save()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )

    def __str__(self):
        return self.content