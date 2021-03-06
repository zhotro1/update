# Generated by Django 3.0.7 on 2020-06-30 00:00

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200629_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='download',
        ),
        migrations.RemoveField(
            model_name='book',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='book',
            name='descriptions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='books/images', validators=[books.models.Book.validate_image]),
        ),
    ]
