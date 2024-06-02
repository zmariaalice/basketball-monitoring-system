from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User
from teams.models import Team
from .models import Player

class PlayerAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser(username='admin', email='admin@test.com', password='password', role='admin')
        self.coach = User.objects.create_user(username='coach', email='coach@test.com', password='password', role='coach')
        
        self.client.login(username='admin', password='password')

        self.team = Team.objects.create(team_name="Test Team", coach=self.coach)
        self.player1 = Player.objects.create(name="Player 1", height=180, average_score=15, games_played=10, team=self.team)
        self.player2 = Player.objects.create(name="Player 2", height=185, average_score=12, games_played=8, team=self.team)
        self.player3 = Player.objects.create(name="Player 3", height=190, average_score=18, games_played=12, team=self.team)

    def test_get_team_players_list(self):
        response = self.client.get(reverse('team-players-list', kwargs={'team_id': self.team.team_id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3) 

    def test_get_top_players(self):
        response = self.client.get(reverse('top-players-list', kwargs={'team_id': self.team.team_id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  

    def tearDown(self):
        self.client.logout()

