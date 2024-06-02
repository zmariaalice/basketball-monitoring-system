from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser(username='admin', email='admin@test.com', password='password', role='admin')
        self.coach = User.objects.create_user(username='coach', email='coach@test.com', password='password', role='coach')
        self.player_user = User.objects.create_user(username='player', email='player@test.com', password='password', role='player')

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(self.admin.role, 'admin')
        self.assertEqual(self.coach.role, 'coach')
        self.assertEqual(self.player_user.role, 'player')

    def test_login(self):
        login = self.client.login(username='admin', password='password')
        self.assertTrue(login)
        self.client.logout()

        login = self.client.login(username='coach', password='password')
        self.assertTrue(login)
        self.client.logout()

        login = self.client.login(username='player', password='password')
        self.assertTrue(login)
        self.client.logout()
