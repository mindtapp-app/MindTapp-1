from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from guardian.admin import GuardedModelAdmin
from .models import GameParticipant

# Register your models here.


# With object permissions support
class GroupAdmin(GuardedModelAdmin):
    pass

admin.site.register(GameParticipant, GroupAdmin)

app_models = apps.get_app_config('common').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass

