# Generated by Django 4.2 on 2023-05-27 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='no title', max_length=1000)),
                ('year', models.IntegerField(default=0)),
                ('genre', models.CharField(default='no genre', max_length=1000)),
                ('director', models.CharField(default='no director', max_length=1000)),
                ('imdbLink', models.URLField(default='https://www.imdb.com/', max_length=1000)),
                ('image', models.ImageField(default='no image', upload_to='images/')),
                ('description', models.CharField(default='no description', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userview.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userview.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
