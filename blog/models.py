from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=100)
    ten = models.FloatField(default=0,max_length=100)
    twelve = models.FloatField(default=0,max_length=100)
    engg = models.FloatField(default=0,max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

