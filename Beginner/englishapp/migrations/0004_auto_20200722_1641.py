# Generated by Django 3.0.7 on 2020-07-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('englishapp', '0003_auto_20200706_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='englishgamescoremodel',
            name='answer',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
