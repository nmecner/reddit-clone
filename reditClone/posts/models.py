from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=150)
    url = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User)
    rating = models.IntegerField(default=0)

    def create_date_pretty(self):
        return self.create_date.strftime('%b %e %Y')