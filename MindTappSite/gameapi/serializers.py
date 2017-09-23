from rest_framework import serializers
from common.models import Game, GameStat, GameParticipant, User, Group
from rest_framework.authtoken.models import Token


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('name', 'participants', 'allowed_orgs')


class GameStatsSerializer(serializers.ModelSerializer):
    #game_session = serializers.RelatedField()

    class Meta:
        model = GameStat
        fields = ('type', 'data', 'game_session')


class GameParticipantSerializer(serializers.ModelSerializer):
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = GameParticipant
        fields = ('id', 'game', 'user')

    #def create(self, validated_data):



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'username')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        #user = User(
        #    email=validated_data['email'],
        #    username=validated_data['username'],
        #)
        user.set_password(validated_data['password'])
        user.save()
        return user

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')

