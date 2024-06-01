from rest_framework import serializers
from .models import Team
from users.serializers import UserSerializer

class TeamSerializer(serializers.Serializer):
    coach = UserSerializer()
    
class Meta:
    model = Team
    fields = ['team_id', 'team_name', 'coach']
