from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import datetime

# Create your models here.


class Game(models.Model):
    name = models.TextField(max_length=128)
    participants = models.ManyToManyField(User, through='GameParticipant')
    allowed_orgs = models.ManyToManyField(Group)

    def __str__(self):
        return self.name


class GameParticipant(models.Model):
    game = models.ForeignKey(Game)
    user = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.game.name + ' ' + self.user.username + ' ' + str(self.date_added)
    #find a prettier way to format date


class GameStat(models.Model):
    type = models.TextField(max_length=64)
    data = models.TextField(max_length=256)
    game_session = models.ForeignKey(GameParticipant, on_delete=models.CASCADE)

    def __str__(self):
        return self.type + ' ' + self.data


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    #todo make tokens expire periodically

#todo: add survey models
