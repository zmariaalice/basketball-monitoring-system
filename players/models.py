from django.db import models
from teams.models import Team

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    height = models.FloatField()
    average_score = models.FloatField()
    games_played = models.IntegerField(default=0)