from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    def __str__(self):
        return self.username


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey('apps.User', on_delete=models.CASCADE, related_name='organized_events')
    participants = models.ManyToManyField('apps.User', related_name='joined_events')


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
