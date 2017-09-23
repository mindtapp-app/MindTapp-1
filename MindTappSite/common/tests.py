from django.test import TestCase
from common.models import User, Group, Game, GameParticipant, GameStat
from rest_framework.test import APIRequestFactory

# Create your tests here.


class GameAPIRunthroughTests(TestCase):
    def setUp(self):
        testgroup = Group.objects.create(name="testgroup")
        game = Game.objects.create(name="Testgame", allowed_orgs=testgroup)

    def fullRun(self):
        factory = APIRequestFactory()
        request = factory.post('/api/register/', {'username': 'newuser', 'password': 'someuserspswd'})
        request = factory.post('/api/api-auth/', {'username': 'newuser', 'password': 'someuserspswd'})
        token = request.data['token']
        request = factory.post('/api/participant_register', )

        # user magically added to the right org todo: implement this



class GameAPIPermissionTests(TestCase):
    def setUp(self):
        Group.objects.create(name="testgroup")
        User.objects.create_user(username="test1user", password="test1userpw")
        User.objects.create_user(username="test2user", password="test2userpw")

