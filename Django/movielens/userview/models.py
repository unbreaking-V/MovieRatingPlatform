from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Movie(models.Model):
    movieid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000, default="no title")
    year = models.IntegerField(default=0)
    genre = models.CharField(max_length=1000, default="no genre")
    director = models.CharField(max_length=1000, default="no director")
    imdblink = models.URLField(max_length=1000, default="https://www.imdb.com/")
    image = models.ImageField(upload_to='images/', default="no image")
    description = models.CharField(max_length=1000, default="no description")

    def __str__(self):
        return self.movieid


class Rating(models.Model):
    value = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comments(models.Model):
    comment = models.CharField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)