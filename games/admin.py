from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['team1', 'team2', 'team1_score', 'team2_score', 'round']
    search_fields = ['team1__team_name', 'team2__team_name']
    list_filter = ['round']
