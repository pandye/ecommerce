from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
