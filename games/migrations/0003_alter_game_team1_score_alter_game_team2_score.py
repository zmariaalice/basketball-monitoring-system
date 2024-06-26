# Generated by Django 5.0.6 on 2024-06-01 03:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0002_alter_game_team1_score_alter_game_team2_score"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="team1_score",
            field=models.IntegerField(
                default=0, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="team2_score",
            field=models.IntegerField(
                default=0, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
