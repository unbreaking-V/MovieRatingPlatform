# Generated by Django 4.2 on 2023-05-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userview', '0004_alter_movie_imdblink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdbLink',
            field=models.URLField(default='https://www.imdb.com/', max_length=1000),
        ),
    ]