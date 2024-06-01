from rest_framework import generics
from django.db.models import Avg
from .models import Team
from .serializers import TeamSerializer
from players.serializers import PlayerSerializer
from players.models import Player

class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamPlayersListView(generics.ListAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        return Player.objects.filter(team_id=team_id)

class TopPlayersListView(generics.ListAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        players = Player.objects.filter(team_id=team_id)
        top_90_percentile = players.aggregate(avg_score=Avg('average_score'))['avg_score'] * 0.9
        return players.filter(average_score__gte=top_90_percentile)
