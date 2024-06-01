from rest_framework import serializers
from .models import Player


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player_id', 'team', 'name', 'height', 'average_score', 'games_played']
