from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import *
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from django.db.models.base import ObjectDoesNotExist

class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    model = User
    permission_classes = (permissions.AllowAny,)


class CreateGameParticipant(generics.CreateAPIView):
    serializer_class = GameParticipantSerializer
    model = GameParticipant
    permission_classes = (permissions.IsAuthenticated,)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class DetailGameParticipant(generics.RetrieveAPIView):
    serializer_class = GameParticipantSerializer
    model = GameParticipant
    permission_classes = (permissions.IsAuthenticated,)
    queryset = GameParticipant.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(GameParticipant, game=self.request.data['game'], user=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj


# todo: allow multiple returns, probably involves not using generic


class GameStatViewSet(viewsets.ModelViewSet):
    serializer_class = GameStatsSerializer
    model = GameStat
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        filter_queryset = GameParticipant.objects.filter(user=user)
        return GameStat.objects.filter(game_session__in=filter_queryset)



# class CreateUser(APIView):
#     permission_classes = [permissions.AllowAny]
#     queryset = User.objects.all()
#
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# class UserViewSet(mixins.CreateModelMixin,
#                  viewsets.GenericViewSet):
#    permissions_classes = [permissions.IsAuthenticated]
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#
#    @method_decorator(csrf_exempt)
#    def dispatch(self, *args, **kwargs):
#        return super(UserViewSet, self).dispatch(*args, **kwargs)

