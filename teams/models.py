from django.db import models
from users.models import User

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name =  models.CharField(max_length=100)
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teams")