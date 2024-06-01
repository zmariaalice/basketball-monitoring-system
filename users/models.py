from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('coach', 'Coach'),
        ('player', 'Player'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    last_login = models.DateTimeField(null=True, blank=True)
    total_time_spent = models.DurationField(default=timedelta)

    def save(self, *args, **kwargs):
        if not self.id and not self.last_login:
            self.last_login = timezone.now()
        super().save(*args, **kwargs)
