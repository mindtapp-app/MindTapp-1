from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib.auth.admin import GroupAdmin
from guardian.admin import GuardedModelAdmin
from .models import *
from django.forms import Textarea

# Register your models here.


class UserInLine(admin.TabularInline):
    model = AccessCodeGroup.user_set.through


class GameInLine(admin.TabularInline):
    model = Game.allowed_orgs.through


class AccessCodeGroupAdmin(GroupAdmin, admin.ModelAdmin):
    list_display = ('name', 'access_code')
    inlines = [UserInLine, GameInLine]

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': '2', 'cols': '50', 'style': 'overflow: hidden;'})},
    }


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': '2', 'cols': '50', 'style': 'overflow: hidden;'})},
    }


class GameStatsAdmin(admin.ModelAdmin):
    list_display = ('game_session', 'type', 'data', 'date_added')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': '2', 'cols': '50', 'style': 'overflow: hidden;'})},
    }


class GameParticipantAdmin(admin.ModelAdmin):
    list_display = ('game', 'user', 'date_added')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': '2', 'cols': '50', 'style': 'overflow: hidden;'})},
    }


class WordInLine(admin.TabularInline):
    model = Word
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': '2', 'cols': '50', 'style': 'overflow: hidden;'})},
    }


class WordListAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    inlines = [
        WordInLine,
    ]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': '2', 'cols': '50', 'style': 'overflow: hidden;'})},
    }


admin.site.register(AccessCodeGroup, AccessCodeGroupAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GameStat, GameStatsAdmin)
admin.site.register(GameParticipant, GameParticipantAdmin)
admin.site.unregister(Group)
admin.site.register(WordList, WordListAdmin)

# in case of not manually registered, pass through all models
app_models = apps.get_app_config('common').get_models()


#for model in app_models:
#    try:
#        admin.site.register(model)
#    except AlreadyRegistered:
#        pass

