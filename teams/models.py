from django.db import models

class Team(models.Model):
    team_id = models.AutoField(primary_key=True, unique=True)
    team_name =  models.CharField(max_length=100)
    coach = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='coached_teams')
    
    def __str__(self):
        return self.team_name