# Generated by Django 5.0.6 on 2024-06-01 03:33

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0001_initial"),
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="player",
            name="player_id",
        ),
        migrations.AddField(
            model_name="player",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=0,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="player",
            name="average_score",
            field=models.FloatField(
                validators=[django.core.validators.MinValueValidator(0.0)]
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="games_played",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="height",
            field=models.FloatField(
                validators=[django.core.validators.MinValueValidator(0.0)]
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="teams.team"
            ),
        ),
    ]
