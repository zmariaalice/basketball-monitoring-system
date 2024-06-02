from django.urls import path
from .views import TeamListCreateView, TeamDetailView, TeamPlayersListView, TopPlayersListView

urlpatterns = [
    path('', TeamListCreateView.as_view(), name='team-list-create'),
    path('<int:team_id>/', TeamDetailView.as_view(), name='team-detail'),
    path('<int:team_id>/players/', TeamPlayersListView.as_view(), name='team-players-list'),
    path('<int:team_id>/top-players/', TopPlayersListView.as_view(), name='top-players-list'),
]
