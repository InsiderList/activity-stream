from actstream import models
from django.contrib import admin

# Use django-generic-admin widgets if available
try:
    from genericadmin.admin import GenericAdminModelAdmin as ModelAdmin
except ImportError:
    ModelAdmin = admin.ModelAdmin

def time_seconds(self, obj):
    return obj.timestamp.strftime("%d %b %Y %H:%M:%S")
time_seconds.admin_order_field = 'timestamp'
time_seconds.short_description = 'Precise Time'

class ActionAdmin(ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = (
    'issuer', '__str__', 'actor', 'verb', 'target', 'action_object',
    'time_seconds')
    list_editable = ('verb',)
    list_filter = ('issuer', 'timestamp', 'verb')
    raw_id_fields = ('actor_content_type', 'target_content_type',
                     'action_object_content_type')


class FollowAdmin(ModelAdmin):
    list_display = (
    '__str__', 'user', 'follow_object', 'actor_only', 'started')
    list_editable = ('user',)
    list_filter = ('user', 'started',)
    raw_id_fields = ('user', 'content_type')


admin.site.register(models.Action, ActionAdmin)
admin.site.register(models.Follow, FollowAdmin)
