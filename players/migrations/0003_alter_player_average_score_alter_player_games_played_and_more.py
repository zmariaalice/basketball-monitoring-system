# Generated by Django 5.0.6 on 2024-06-01 03:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0002_remove_player_player_id_player_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="average_score",
            field=models.FloatField(
                default=0.0, validators=[django.core.validators.MinValueValidator(0.0)]
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="games_played",
            field=models.IntegerField(
                default=0, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="height",
            field=models.FloatField(
                default=0.0, validators=[django.core.validators.MinValueValidator(0.0)]
            ),
        ),
    ]
