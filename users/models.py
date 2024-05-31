from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('coach', 'Coach'),
        ('player', 'Player'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    last_login = models.DateTimeField(null=True, blank=True)
    total_time_spent = models.PositiveBigIntegerField(default=0) # going to be in minutes