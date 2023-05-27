from django.contrib import admin
from .models import Rating, Comments, Movie

admin.site.register(Movie)
admin.site.register(Comments)
admin.site.register(Rating)