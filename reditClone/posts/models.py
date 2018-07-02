from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=150)
    url = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User)
    rating = models.IntegerField(default=0)