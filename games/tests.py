from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User
from teams.models import Team
from games.models import Game

class GameAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser(username='admin', email='admin@test.com', password='password', role='admin')
        self.coach1 = User.objects.create_user(username='coach1', email='coach1@test.com', password='password', role='coach')
        self.coach2 = User.objects.create_user(username='coach2', email='coach2@test.com', password='password', role='coach')
        
        self.client.login(username='admin', password='password')

        self.team_a = Team.objects.create(team_name="Team A", coach=self.coach1)
        self.team_b = Team.objects.create(team_name="Team B", coach=self.coach2)

        self.game = Game.objects.create(team1=self.team_a, team2=self.team_b, team1_score=85, team2_score=90)

    def test_get_all_games(self):
        response = self.client.get(reverse('game-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    # def test_get_game_detail(self):
    #     response = self.client.get(reverse('game-detail', kwargs={'game_id': self.game.game_id}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data['team1'], self.game.team_a_score)
    #     self.assertEqual(response.data['team2'], self.game.team_b_score)

    # def test_create_new_game(self):
    #     data = {'team2': self.team_a.team_id, 'team2': self.team_b.team_id, 'team1_score': 75, 'team2_score': 80}
    #     response = self.client.post(reverse('game-list-create'), data, format='json')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertTrue(Game.objects.filter(team1=self.team_a, team2=self.team_b, team1_score=75, team2_score=80).exists())

    def tearDown(self):
        self.client.logout()
