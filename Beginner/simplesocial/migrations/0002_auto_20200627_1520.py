# Generated by Django 3.0.7 on 2020-06-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplesocial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persion',
            name='persion_img',
            field=models.ImageField(upload_to='persions/images'),
        ),
        migrations.AlterField(
            model_name='persion',
            name='persion_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]