from teams.models import Team

teams_data = [
    {"team_name": "Pacheco Basketball Team"},
    {"team_name": "Bennett Basketball Team"},
    {"team_name": "Russell Basketball Team"},
    {"team_name": "Welch Basketball Team"},
    {"team_name": "Thornton Basketball Team"},
    {"team_name": "Guzman Basketball Team"},
    {"team_name": "Cummings Basketball Team"},
    {"team_name": "Thomas Basketball Team"},
    {"team_name": "Knight Basketball Team"},
    {"team_name": "Wilson Basketball Team"},
    {"team_name": "Sanders Basketball Team"},
    {"team_name": "Cooke Basketball Team"},
    {"team_name": "Ross Basketball Team"},
    {"team_name": "Hunter Basketball Team"},
    {"team_name": "Gonzalez Group Basketball Team"},
    {"team_name": "Clark Basketball Team"}
]

for team_data in teams_data:
    Team.objects.get_or_create(**team_data)


