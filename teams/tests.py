from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User
from .models import Team

class TeamAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser(username='admin', email='admin@test.com', password='password', role='admin')
        self.coach = User.objects.create_user(username='coach', email='coach@test.com', password='password', role='coach')
        
        self.client.login(username='admin', password='password')

        self.team = Team.objects.create(team_name="Test Team", coach=self.coach)

    def test_get_all_teams(self):
        response = self.client.get(reverse('team-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def tearDown(self):
        self.client.logout()