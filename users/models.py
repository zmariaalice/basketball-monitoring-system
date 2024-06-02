from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('coach', 'Coach'),
        ('player', 'Player'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    last_login = models.DateTimeField(null=True, blank=True)
    total_time_spent = models.DurationField(default=timedelta)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    team = models.ForeignKey('teams.Team', on_delete=models.SET_NULL, null=True, blank=True, db_column='team_name')

    def save(self, *args, **kwargs):
        if not self.id and not self.last_login:
            self.last_login = timezone.now()
        super().save(*args, **kwargs)

    @receiver(post_save, sender=get_user_model())
    def create_player(sender, instance, created, **kwargs):
        if created and instance.role == 'player':
            from players.models import Player
            Player.objects.create(team=instance.team, name=instance.username)
