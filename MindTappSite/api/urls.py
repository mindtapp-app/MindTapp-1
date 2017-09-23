from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^survey/$', views.SurveyList.as_view()),
    url(r'^survey/(?P<pk>[0-9]+)$', views.SurveyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
