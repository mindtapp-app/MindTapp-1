from django.test import TestCase
from common.models import User, Group, Game, GameParticipant, GameStat
from rest_framework.test import APIRequestFactory, APIClient

# Create your tests here.


class GameAPIRegisterTests(TestCase):
    def setUp(self):
        # testgroup = Group.objects.create(name="testgroup")
        # game = Game.objects.create(name="Testgame", allowed_orgs='testgroup')
        self.client = APIClient()

    def test_minimal_fields(self):
        request = self.client.post('/api/register/', {'username': 'newuser',
                                                  'password': 'someuserpswd'})
        self.assertEqual(User.objects.filter(username='newuser').exists(), True)

    def test_all_fields(self):
        request = self.client.post('/api/register/', {'username': 'newuser',
                                                  'password': 'someuserpswd',
                                                  'email': 'test@example.com',
                                                  'first_name': 'bob',
                                                  'last_name': 'test'})
        self.assertEqual(User.objects.filter(username='newuser').exists(), True)

    def test_user_in_default_group(self):
        request = self.client.post('/api/register/', {'username': 'newuser',
                                                  'password': 'someuserspswd'})
        self.assertEqual(User.objects.filter(username='newuser', groups__name='defaultgameusers').exists(), True)

    def test_missing_information(self):
        request = self.client.post('/api/register/', {})
        self.assertEqual(request.status_code, 400)


class GameAPITokenAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_then_obtain(self):
        self.client.post('/api/register/', {'username': 'newuser',
                                                      'password': 'someuserpswd'})
        request = self.client.post('/api/api-auth/', {"username": "newuser",
                                                      "password": "someuserpswd"})
        self.assertEqual(request.status_code, 200)


# class GameAPIPermissionTests(TestCase):
#     def setUp(self):
#         Group.objects.create(name="testgroup")
#         User.objects.create_user(username="test1user", password="test1userpw")
#         User.objects.create_user(username="test2user", password="test2userpw")

