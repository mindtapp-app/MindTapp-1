from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'contact_email'
urlpatterns = [
    url(r'^$', views.contact, name='contact'),
]
