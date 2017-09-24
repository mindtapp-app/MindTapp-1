from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib.auth.admin import GroupAdmin
from guardian.admin import GuardedModelAdmin
from .models import *

# Register your models here.


# With object permissions support
class AccessCodeGroupAdmin(GroupAdmin, admin.ModelAdmin):
    list_display = ('name', 'access_code')


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class GameStatsAdmin(admin.ModelAdmin):
    list_display = ('game_session', 'type', 'data')


class GameParticipantAdmin(admin.ModelAdmin):
    list_display = ('game', 'user', 'date_added')


admin.site.register(AccessCodeGroup, AccessCodeGroupAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GameStat, GameStatsAdmin)
admin.site.register(GameParticipant, GameParticipantAdmin)

app_models = apps.get_app_config('common').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass

