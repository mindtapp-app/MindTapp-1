from .serializers import *
from rest_framework import generics, permissions, status, response
from rest_framework import viewsets


class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    model = User
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        if not Group.objects.filter(name="defaultgameusers").exists():
            Group.objects.create(name="defaultgameusers")

        serializer.save()

        group = Group.objects.get(name="defaultgameusers")
        group.user_set.add(User.objects.get(username=self.request.data["username"]))


class CreateGameParticipant(generics.CreateAPIView):
    serializer_class = GameParticipantSerializer
    model = GameParticipant
    permission_classes = (permissions.IsAuthenticated,)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if GameParticipant.objects.filter(user=self.request.user, game=self.request.data['game']).exists():
            return response.Response({'error': 'entry already exists'}, status.HTTP_400_BAD_REQUEST)

        return super(CreateGameParticipant, self).create(*args, **kwargs)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# todo: combine game participants into a single listcreateapiview
class DetailGameParticipant(generics.ListAPIView):
    serializer_class = GameParticipantSerializer
    model = GameParticipant
    permission_classes = (permissions.IsAuthenticated,)
    queryset = GameParticipant.objects.all()

    def list(self, request, *args, **kwargs):
        if 'game' not in self.request.data:
            return response.Response(data={'error': 'game not provided'}, status=status.HTTP_400_BAD_REQUEST)

        if not Game.objects.filter(id=self.request.data['game']).exists():
            return response.Response(data={'error': 'game doesnt exist'}, status=status.HTTP_400_BAD_REQUEST)

        return super(DetailGameParticipant, self).list(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        if 'game' not in self.request.data:
            return GameParticipant.objects.none()
        game = self.request.data['game']

        return GameParticipant.objects.filter(user=user, game=game)

    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     obj = get_object_or_404(GameParticipant, game=self.request.data['game'], user=self.request.user)
    #     self.check_object_permissions(self.request, obj)
    #     return obj


# todo: allow multiple returns, probably involves not using generic


class GameStatViewSet(viewsets.ModelViewSet):
    serializer_class = GameStatsSerializer
    model = GameStat
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if 'game' not in self.request.data:
            return response.Response({'error': 'game not provided'}, status=status.HTTP_400_BAD_REQUEST)

        return super(GameStatViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(game_session=GameParticipant.objects.get(game=self.request.data['game'], user=self.request.user))

    def get_queryset(self):
        user = self.request.user
        filter_queryset = GameParticipant.objects.filter(user=user)
        return GameStat.objects.filter(game_session__in=filter_queryset)


