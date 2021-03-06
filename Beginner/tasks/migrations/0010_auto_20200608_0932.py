# Generated by Django 3.0.6 on 2020-06-08 02:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0009_auto_20180507_0328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='username',
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('adanger', 'Ưu tiên cao'), ('bwarning', 'Ưu tiên vừa'), ('csuccess', 'Ưu tiên thấp')], default='adanger', max_length=30),
        ),
        migrations.DeleteModel(
            name='Username',
        ),
    ]
