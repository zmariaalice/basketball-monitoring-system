from django.db import models
from teams.models import Team

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    team1 =  models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1_games')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2_games')
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    round_choices = [
        ('qualifying', 'Qualifying'),
        ('quarter-final', 'Quarter-Final'),
        ('semi-final', 'Semi-Final'),
        ('final', 'Final'),
        
    ]
    round = models.CharField(max_length=20, choices=round_choices)
