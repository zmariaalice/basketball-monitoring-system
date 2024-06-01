from django.db import models
from django.core.validators import MinValueValidator
from teams.models import Team

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    height = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)
    average_score = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)
    games_played = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.name