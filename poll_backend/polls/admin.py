
# Register your models here.
from django.contrib import admin
from .models import Poll, Option

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at', 'expires_at')
    search_fields = ('question',)

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'poll', 'votes')
    list_filter = ('poll',)
