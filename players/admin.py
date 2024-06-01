from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'team', 'height', 'average_score', 'games_played']
    search_fields = ['name']
    list_filter = ['team']
