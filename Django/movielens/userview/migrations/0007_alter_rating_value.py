# Generated by Django 4.2 on 2023-05-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userview', '0006_rename_imdblink_movie_imdblink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.FloatField(),
        ),
    ]
