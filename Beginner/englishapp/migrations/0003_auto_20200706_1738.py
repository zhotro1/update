# Generated by Django 3.0.7 on 2020-07-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('englishapp', '0002_englishgamescoremodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='englishgamescoremodel',
            name='answer',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='englishgamescoremodel',
            name='time_update_key',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='englishgamescoremodel',
            name='time_update_score',
            field=models.FloatField(default=0),
        ),
    ]
