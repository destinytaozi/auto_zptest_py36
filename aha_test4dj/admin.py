from django.contrib import admin
from aha_test4dj.models import Event, Guest


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
