from rest_framework import serializers
from common.models import Game, GameStat, GameParticipant, User, AccessCodeGroup, WordList, Word
from rest_framework.authtoken.models import Token


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('word',)


class WordListSerializer(serializers.ModelSerializer):
    # words = WordSerializer(many=True, read_only=True)
    words = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = WordList
        fields = ('name', 'words')


class AccessCodeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessCodeGroup
        fields = ('name', 'access_code')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('name', 'participants', 'allowed_orgs')

# class GameStatsPostSerializer(serializers.ModelSerializer):
#


class GameStatsSerializer(serializers.ModelSerializer):
    game_session = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = GameStat
        fields = ('type', 'data', 'game_session')
        # extra_kwargs = {'game': {'read_only': True}}


class GameParticipantSerializer(serializers.ModelSerializer):
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    game_stats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = GameParticipant
        fields = ('id', 'game', 'user', 'game_stats')

    #def create(self, validated_data):



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'username')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')

