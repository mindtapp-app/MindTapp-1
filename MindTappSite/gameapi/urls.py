from django.conf.urls import url, include
from rest_framework import routers
from . import views
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register(r'stats', views.GameStatViewSet, base_name='game stat')

urlpatterns = [
    url(r'^register', csrf_exempt(views.CreateUser.as_view())),
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^participant_register', csrf_exempt(views.CreateGameParticipant.as_view())),
    url(r'^participant_details/(?P<name>[\w\-]+)', csrf_exempt(views.DetailGameParticipant.as_view())),
    url(r'^access/$', csrf_exempt(views.AddGroup.as_view())),
    url(r'^access/(?P<name>[\w\-]+)', csrf_exempt(views.CheckGroup.as_view())),
    url(r'^wordlist/(?P<name>[\w\-]+)', csrf_exempt(views.RetrieveWordList.as_view())),
    url(r'^', include(router.urls)),
]

from rest_framework.authtoken import views
urlpatterns += [url(r'^api-auth/', views.obtain_auth_token)]
