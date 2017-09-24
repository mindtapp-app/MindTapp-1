from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import datetime
import random
from django.db import IntegrityError

# Create your models here.


class Game(models.Model):
    name = models.TextField(max_length=128)
    participants = models.ManyToManyField(User, through='GameParticipant')
    allowed_orgs = models.ManyToManyField(Group)

    def __str__(self):
        return str(self.id) + ': ' + self.name


class GameParticipant(models.Model):
    game = models.ForeignKey(Game)
    user = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.game.name + ', ' + self.user.username + ', ' + str(self.date_added)
    #find a prettier way to format date


class GameStat(models.Model):
    type = models.TextField(max_length=64)
    data = models.TextField(max_length=256)
    game_session = models.ForeignKey(GameParticipant, on_delete=models.CASCADE, related_name='game_stats')

    def __str__(self):
        return '(' + self.game_session.user.username + ') ' + self.type + ': ' + self.data


# todo continue working on group access code
class AccessCodeGroup(Group):
    access_code = models.CharField(max_length=16, blank=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.access_code:
            self.access_code = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
        success = False
        failures = 0
        while not success:
            try:
                super(AccessCodeGroup, self).save(*args, **kwargs)
            except IntegrityError:
                failures += 1
                if failures > 5:  # or some other arbitrary cutoff point at which things are clearly wrong
                    raise
                else:
                    # looks like a collision, try another random value
                    self.access_code = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
            else:
                success = True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    #todo make tokens expire periodically

#todo: add survey models
